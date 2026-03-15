# Ray Cluster — Troubleshooting Notes

Hard-won lessons from getting Ray + multi-GPU DDP working on a multi-node GPU cluster.

## Cluster Startup

```bash
# Head node
PYTHON/bin/ray start --head --port=6379 \
  --temp-dir=/tmp/$USER/ray --num-gpus=4

# Worker node (--temp-dir is ignored on workers, they inherit from head)
PYTHON/bin/ray start --address=<head-ip>:6379 --num-gpus=4
```

## Critical: temp-dir Must Be Node-Local

**Problem:** If `--temp-dir` points to a shared filesystem, Ray creates raylet Unix domain
sockets on the shared path. Both nodes write their sockets (`raylet`, `raylet.1`) to the
same directory. Unix domain sockets are node-local — node 1 cannot connect to node 2's
`raylet.1` even though the file is visible via the shared filesystem.

**Symptom:**
```
Could not connect to socket .../sockets/raylet.1
*** StackTrace: ray::raylet::RayletConnection::RayletConnection()
```

**Fix:** Use a node-local temp dir:
```bash
ray start --head --temp-dir=/tmp/$USER/ray ...
```

## Task Scheduling

- Ray schedules `@ray.remote` tasks on whichever node has available resources
- With 4 GPUs on each node, a `num_gpus=4` task can run on either node
- GPU usage will appear on the node where the task was scheduled, NOT necessarily the head
- To see which node a task runs on: `socket.gethostname()` inside the remote function
- To see GPU usage: `nvidia-smi` on the node where the task is running

## Multi-GPU DDP Approaches

### What Works: @ray.remote(num_gpus=4) + mp.fork + single-node DDP

```python
@ray.remote(num_gpus=4, num_cpus=16)
def train(lr, ...):
    import torch.multiprocessing as mp
    ctx = mp.get_context("fork")   # fork, NOT spawn
    q = ctx.Queue()
    processes = [ctx.Process(target=_worker, args=(rank, 4, q, lr, ...)) for rank in range(4)]
    for p in processes: p.start()
    for p in processes: p.join()
    return q.get()
```

Key points:
- Use `mp.get_context("fork")` — NOT "spawn"
- "spawn" fails with `PicklingError: Can't pickle <function _worker>` because
  inside a Ray task, `__main__` is the Ray worker, not your script
- `fork` copies the parent process memory so `_worker` is accessible without pickling
- `_worker` must be defined at module level (not inside the Ray remote function)
- Each forked process sees all 4 GPUs (Ray sets CUDA_VISIBLE_DEVICES=0,1,2,3)
- Use `torch.cuda.set_device(rank)` and `device = torch.device(f"cuda:{rank}")`
- Use `init_method="tcp://127.0.0.1:29500"` for the dist process group

### What Does NOT Work: Cross-Node DDP (8 GPUs on 2 nodes)

**Problem:** NCCL detects "duplicate GPU" when both nodes have identical hardware.
NCCL compares PCIe bus IDs to identify GPUs. On clusters where GPU 0 on node 1 and
GPU 0 on node 2 have the same PCIe bus ID (identical hardware), NCCL flags this as
an error even though they are physically different GPUs.

**Symptom:**
```
ncclInvalidUsage: Duplicate GPU detected: rank 0 and rank 4 both on CUDA device 3000
```

**Things that don't fix it:**
- `NCCL_P2P_DISABLE=1`
- `NCCL_SOCKET_IFNAME=hsn`
- `dist.init_process_group(..., device_id=device)`
- Ray Train's TorchTrainer (also fails — different error path, same root cause)

**Workaround:** Use single-node 4-GPU DDP only (`num_gpus=4` per Ray task).

### What Does NOT Work: Ray Train TorchTrainer (with shared filesystem temp-dir)

```python
TorchTrainer(train_loop, ScalingConfig(num_workers=8, use_gpu=True))
```

Fails with `Could not connect to socket .../raylet.1` when temp-dir is on shared filesystem.
Fix: use `/tmp/$USER/ray` as temp-dir.

## DDP: Single-Rank Inference Deadlock

**Problem:** Calling `model(x)` on the DDP wrapper inside an `if rank == 0:` block fires
NCCL collective hooks. Other ranks are not in the block so they never call a matching
collective — deadlock after 10 minutes.

**Fix:** Use `model.module(x)` for any single-rank inference (val/test):
```python
if rank == 0:
    model.module.eval()
    with torch.no_grad():
        pred = model.module(x)   # NOT model(x)
    model.module.train()         # restore before next DDP backward
```

## Verifying GPU Usage

GPU utilization is only visible on the node where the task runs:

```python
@ray.remote(num_gpus=4)
def check():
    import subprocess, socket
    r = subprocess.run(['nvidia-smi', '--query-gpu=index,utilization.gpu,memory.used',
                        '--format=csv,noheader'], capture_output=True, text=True)
    return {'node': socket.gethostname(), 'gpus': r.stdout.strip()}
```

Memory allocated (even at 0% compute) confirms CUDA context is active.

## Prometheus + Grafana (Ray Dashboard Time-Series Charts)

The Ray dashboard at http://127.0.0.1:8265 shows "Time-series charts are hidden" until
Prometheus and Grafana are running. Ray generates all config files automatically.

### Start Prometheus

```bash
PYTHON/bin/ray metrics launch-prometheus
# Downloads binary on first run, then starts it
# Prometheus available at http://localhost:9090
```

### Fix session_latest symlink (if broken)

```bash
ls /tmp/$USER/ray/   # find actual session dir name
ln -sfn /tmp/$USER/ray/session_YYYY-MM-DD_... /tmp/$USER/ray/session_latest
```

### Download and Start Grafana

Ray generates Grafana config but not the binary. Download once to a persistent location:

```bash
curl -s "https://dl.grafana.com/oss/release/grafana-11.5.2.linux-amd64.tar.gz" \
  -o /path/to/grafana.tar.gz
tar -xzf /path/to/grafana.tar.gz -C /path/to/grafana/
```

Start with Ray's pre-generated config:

```bash
mkdir -p /tmp/$USER/ray/grafana_data
nohup /path/to/grafana/grafana-11.5.2/bin/grafana server \
  --config /tmp/$USER/ray/session_latest/metrics/grafana/grafana.ini \
  --homepath /path/to/grafana/grafana-11.5.2 \
  cfg:default.paths.data=/tmp/$USER/ray/grafana_data \
  cfg:default.server.http_port=3000 \
  > /tmp/$USER/ray/grafana.log 2>&1 &
```

### Restart Ray Dashboard to Pick Up Grafana

The dashboard discovers Grafana at startup only. If already running, restart it:

```bash
kill $(pgrep -f "dashboard/dashboard.py")

# Get the exact args from the original process first:
# cat /proc/<pid>/cmdline | tr '\0' ' '
# Then restart with the same args. Dashboard auto-discovers Grafana at localhost:3000.
```

Verify:
```bash
curl -s http://127.0.0.1:8265/api/prometheus_health
curl -s http://127.0.0.1:8265/api/grafana_health
# Both should return: {"result": true, ...}
```

## Runtime Environment

Always ship code to workers:
```python
ray.init(address="auto", runtime_env={"working_dir": os.path.dirname(os.path.abspath(__file__))})
```

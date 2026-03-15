# train.py Templates — Ray Boilerplate

The generated `train.py` is read-only boilerplate. The user's model lives in `model.py`.
Autoresearch scope is always `model.py`, never `train.py`.

## File Structure

```
model.py    ← autoresearch modifies this
train.py    ← generated once, never touched again
```

## Two Templates

| Template | When to use |
|----------|-------------|
| [Single-GPU / Fractional](#single-gpu-template) | Custom DataLoaders, multi-input models, existing `train_main()` function, small models (< a few GB VRAM). Supports fractional GPU (`num_gpus=0.5`) to run 2 tasks per GPU simultaneously. |
| [Multi-GPU DDP](#multi-gpu-ddp-template) | CIFAR-style image classification, models that benefit from 4-GPU data parallelism |

### Adaptive GPU Allocation (recommended)

Start with `num_gpus=0.5` to pack 2 experiments per GPU. If the model causes OOM, automatically retry with a full GPU. This requires two pre-declared remote functions (Ray resource allocation is fixed at decoration time) and an OOM-aware wrapper in `main()`:

```python
def _run_training(mem_fraction):
    import torch
    if mem_fraction is not None:
        torch.cuda.set_per_process_memory_fraction(mem_fraction, 0)
    # ... all training logic here, using cuda:0

@ray.remote(num_gpus=0.5)
def _train_half_gpu():
    return _run_training(mem_fraction=0.45)   # ~18GB of 40GB

@ray.remote(num_gpus=1.0)
def _train_full_gpu():
    return _run_training(mem_fraction=None)   # full 40GB

def _is_oom(exc):
    return "OutOfMemoryError" in str(exc) or "CUDA out of memory" in str(exc)

def main():
    ray.init(address="auto", runtime_env={"working_dir": ...})
    try:
        result = ray.get(_train_half_gpu.remote())
    except ray.exceptions.RayTaskError as e:
        if _is_oom(e):
            print("OOM at 0.5 GPU — retrying with full GPU", flush=True)
            result = ray.get(_train_full_gpu.remote())
        else:
            raise
    print(f"val_acc={result:.4f}")
```

| num_gpus | Tasks per GPU | Total (8-GPU cluster) | VRAM budget per task |
|----------|---------------|----------------------|---------------------|
| 0.5      | 2             | 16                   | ~18 GB (cap at 0.45)|
| 1.0      | 1             | 8                    | 40 GB (no cap)      |

**Rule**: `mem_fraction` should be slightly below `num_gpus` to leave headroom (e.g. `0.45` for `0.5`). Ray sets `CUDA_VISIBLE_DEVICES` per task, so `cuda:0` inside the task always refers to the assigned physical GPU.

---

## Single-GPU Template

Use this when:
- Your model has custom data loading (CSV, numpy arrays, HDF5, etc.)
- Your model takes multiple inputs (e.g. historical context + future covariates)
- You already have a `train_main()` function you want to wrap with Ray
- 1 GPU is sufficient for your model size

### model.py Contract (Single-GPU)

Must export a class named `Model`. No fixed signature — adapt to your inputs:

```python
# Single-input example
class Model(nn.Module):
    def __init__(self, input_size, hidden_size=128, output_size=1):
        super().__init__()
        ...
    def forward(self, x):
        # x: [B, T, features]
        return output  # [B] or [B, H]

# Multi-input example (e.g. historical + future covariates)
class Model(nn.Module):
    def __init__(self, hist_features, future_features, hidden_size=128, forecast_horizon=6):
        super().__init__()
        ...
    def forward(self, x_hist, x_future):
        # x_hist: [B, T, hist_features]
        # x_future: [B, H, future_features]
        return predictions  # [B, H]
```

### train.py Template (Single-GPU, adaptive)

```python
"""
Single-GPU Ray trainer — DO NOT MODIFY (boilerplate).
Autoresearch scope: model.py

GPU strategy: tries 0.5 GPU first (2 tasks/GPU). Falls back to full GPU on OOM.
"""

import os
import ray

os.environ["RAY_DEDUP_LOGS"] = "0"

CONFIG_PATH = "{{CONFIG_PATH}}"
OUTPUT_DIR  = "{{OUTPUT_DIR}}"


def _run_training(config, mem_fraction):
    import sys, torch
    if mem_fraction is not None:
        torch.cuda.set_per_process_memory_fraction(mem_fraction, 0)
    sys.path.insert(0, config["working_dir"])

    # train_main must return a scalar metric (higher = better)
    from train_fn import train_main
    return float(train_main(config["config_path"], config["output_dir"]))


@ray.remote(num_gpus=0.5)
def _train_half(config):
    return _run_training(config, mem_fraction=0.45)


@ray.remote(num_gpus=1.0)
def _train_full(config):
    return _run_training(config, mem_fraction=None)


def _is_oom(exc):
    return "OutOfMemoryError" in str(exc) or "CUDA out of memory" in str(exc)


def main():
    config = {
        "working_dir": os.path.dirname(os.path.abspath(__file__)),
        "config_path": CONFIG_PATH,
        "output_dir": OUTPUT_DIR,
    }
    ray.init(address="auto", runtime_env={"working_dir": config["working_dir"]})
    try:
        val_acc = ray.get(_train_half.remote(config))
    except ray.exceptions.RayTaskError as e:
        if _is_oom(e):
            print("OOM at 0.5 GPU — retrying with full GPU", flush=True)
            val_acc = ray.get(_train_full.remote(config))
        else:
            raise
    print(f"val_acc={val_acc:.4f}")

if __name__ == "__main__":
    main()
```

### Adapting an Existing train_main()

If you already have a training function with a different signature, write a thin adapter:

```python
# adapter in train_fn.py — import this from train.py
def train_main(config_path, output_dir):
    # Call your existing function
    mse, mae, rmse, r2, ioa = your_existing_train(config_path, output_dir)
    # Return the metric autoraysearch should maximize
    # Example: composite of R² and Index of Agreement
    return (r2 + ioa) / 2
```

The metric must be a float where **higher is better**. If your metric is lower-is-better (e.g. MSE), negate it: `return -mse`.

### Injecting Model from model.py

Your `train_main` (or your model-building code) must import `Model` from `model.py`:

```python
# Inside your train_main or model-building function:
import sys, os
sys.path.insert(0, working_dir)
from model import Model

model = Model(hist_features=8, future_features=6, hidden_size=128).to(device)
```

Autoraysearch modifies `model.py` and re-runs `train.py` each iteration. The import must happen inside the function (not at module level) so each run picks up the latest version.

---

## Multi-GPU DDP Template

Use this for models that benefit from 4-GPU data parallelism (image classification, large batch training).

### model.py Contract (Multi-GPU DDP)

Must export a class named `Model` that accepts `num_classes=N`:

```python
class Model(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        ...
    def forward(self, x):
        ...
```

### train.py Template (Multi-GPU DDP)

```python
"""
Multi-GPU Ray + DDP trainer — DO NOT MODIFY (boilerplate).
Autoresearch scope: model.py
...
"""

import os
import ray

os.environ["RAY_DEDUP_LOGS"] = "0"

# Configuration — edit these to change dataset / training schedule
DATASET      = "CIFAR10"   # CIFAR10 | CIFAR100
LR           = 0.05
EPOCHS       = 20
BATCH_SIZE   = 256          # per GPU
MOMENTUM     = 0.9
WEIGHT_DECAY = 1e-4
NUM_GPUS     = 4
DATA_DIR     = "{{DATA_DIR}}"

_DATASET_CFG = {
    "CIFAR10":  {"num_classes": 10,  "mean": (0.4914, 0.4822, 0.4465), "std": (0.2023, 0.1994, 0.2010)},
    "CIFAR100": {"num_classes": 100, "mean": (0.5071, 0.4867, 0.4408), "std": (0.2675, 0.2565, 0.2761)},
}


def _worker(rank, world_size, result_queue, config):
    import torch, torch.nn as nn, torch.optim as optim
    import torch.distributed as dist
    from torch.nn.parallel import DistributedDataParallel as DDP
    from torch.utils.data import DataLoader, DistributedSampler
    import torchvision.datasets as tvdsets
    import torchvision.transforms as T
    import sys

    sys.path.insert(0, os.getcwd())
    from model import Model

    dist.init_process_group("nccl", rank=rank, world_size=world_size,
                            init_method="tcp://127.0.0.1:29500")
    torch.cuda.set_device(rank)
    device = torch.device(f"cuda:{rank}")

    cfg     = _DATASET_CFG[config["dataset"]]
    ds_cls  = getattr(tvdsets, config["dataset"])

    transform_train = T.Compose([
        T.RandomHorizontalFlip(), T.RandomCrop(32, padding=4),
        T.ToTensor(), T.Normalize(cfg["mean"], cfg["std"]),
    ])
    transform_val = T.Compose([T.ToTensor(), T.Normalize(cfg["mean"], cfg["std"])])

    train_ds = ds_cls(config["data_dir"], train=True,  download=True, transform=transform_train)
    val_ds   = ds_cls(config["data_dir"], train=False, download=True, transform=transform_val)

    train_loader = DataLoader(train_ds, batch_size=config["batch_size"],
                              sampler=DistributedSampler(train_ds, world_size, rank),
                              num_workers=4, pin_memory=True)
    val_loader   = DataLoader(val_ds, batch_size=config["batch_size"] * 2,
                              shuffle=False, num_workers=4, pin_memory=True)

    model     = DDP(Model(num_classes=cfg["num_classes"]).to(device), device_ids=[rank])
    optimizer = optim.SGD(model.parameters(), lr=config["lr"],
                          momentum=config["momentum"], weight_decay=config["weight_decay"])
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=config["epochs"])
    criterion = nn.CrossEntropyLoss()

    for epoch in range(config["epochs"]):
        model.train()
        train_loader.sampler.set_epoch(epoch)
        for X, y in train_loader:
            X, y = X.to(device), y.to(device)
            optimizer.zero_grad()
            criterion(model(X), y).backward()
            optimizer.step()
        scheduler.step()

    dist.barrier()  # sync before eval
    if rank == 0:
        model.module.eval()  # .module bypasses DDP — avoids NCCL ALLREDUCE deadlock
        correct = total = 0
        with torch.no_grad():
            for X, y in val_loader:
                X, y = X.to(device), y.to(device)
                correct += (model.module(X).argmax(1) == y).sum().item()
                total   += len(y)
        result_queue.put(correct / total)

    dist.destroy_process_group()


@ray.remote(num_gpus=NUM_GPUS, num_cpus=NUM_GPUS * 4)
def _train_remote(config):
    import torch.multiprocessing as mp
    ctx = mp.get_context("fork")   # fork NOT spawn — spawn fails inside Ray tasks
    result_queue = ctx.Queue()
    processes = [ctx.Process(target=_worker, args=(rank, config["num_gpus"], result_queue, config))
                 for rank in range(config["num_gpus"])]
    for p in processes: p.start()
    for p in processes: p.join()
    return result_queue.get()


def main():
    config = {
        "dataset": DATASET, "lr": LR, "epochs": EPOCHS, "batch_size": BATCH_SIZE,
        "momentum": MOMENTUM, "weight_decay": WEIGHT_DECAY,
        "num_gpus": NUM_GPUS, "data_dir": DATA_DIR,
    }
    ray.init(address="auto", runtime_env={"working_dir": os.path.dirname(os.path.abspath(__file__))})
    val_acc = ray.get(_train_remote.remote(config))
    print(f"val_acc={val_acc:.4f}")

if __name__ == "__main__":
    main()
```

## Supported Datasets (DDP Template)

| DATASET value | Classes | Notes |
|--------------|---------|-------|
| CIFAR10 | 10 | auto-downloaded to DATA_DIR |
| CIFAR100 | 100 | auto-downloaded to DATA_DIR |

For custom datasets with the DDP template: add an entry to `_DATASET_CFG` and implement the `ds_cls` logic in `_worker`. For fully custom data pipelines, use the Single-GPU template instead.

## Key Implementation Notes

- Use `mp.get_context("fork")` — NOT "spawn". Spawn fails with PicklingError inside Ray tasks.
- `_worker` must be defined at module level (not inside the Ray remote function) for fork to find it.
- `sys.path.insert(0, os.getcwd())` is needed so `from model import Model` works in the Ray worker.
- `init_method="tcp://127.0.0.1:29500"` — single-node DDP, all 4 GPUs on one node.
- **DDP deadlock**: Use `model.module.eval()` and `model.module(X)` in rank-0-only eval blocks. Calling `model(X)` (the DDP wrapper) triggers NCCL ALLREDUCE — but only rank 0 participates, so all other ranks hang waiting. `model.module` bypasses DDP and runs purely local inference.
- `dist.barrier()` before the rank-0 eval block ensures all training is done before rank 0 starts eval, while ranks 1–3 safely proceed to `dist.destroy_process_group()`.
- Cross-node 8-GPU DDP may fail on clusters where nodes have identical PCIe bus IDs (see ray-cluster.md).
- See `ray-cluster.md` for full cluster setup and troubleshooting.

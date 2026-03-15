# Setup Protocol — autoraysearch

Run once before starting the loop. Goal: generate a working train.py and establish a baseline.

## Step 1: Get Model File

Ask user for the model file path. Read it fully.

The file must contain an `nn.Module` subclass. Identify:
- Class name (e.g., `CNN`, `ResNet`, `MyModel`)
- `__init__` signature (what hyperparameters does it take?)
- `forward` signature (input shape?)
- Any hardcoded hyperparameters inside the class

## Step 2: Get Dataset Info

Ask user for the dataset. Options:
- CIFAR-10 (default, auto-downloaded)
- CIFAR-100
- ImageNet (ask for path)
- Custom (ask for DataLoader code or path)

Record:
- `DATA_DIR` path
- Input shape (e.g., 3x32x32 for CIFAR-10)
- Number of classes

## Step 3: Get Cluster Config

Ask or infer:
- `NUM_WORKERS`: total GPUs across all nodes (default: 8 for 2x4-GPU setup)
- `RAY_ADDRESS`: usually "auto" if cluster is already running
- `PYTHON`: path to Python binary with Ray + PyTorch installed
- GPU allocation per experiment — ask the user:
  ```
  How much GPU should each experiment get?
    A) 1 GPU per experiment (default — safest)
    B) 0.5 GPU — 2 experiments share one GPU (2x more parallel, auto-falls back on OOM)
  ```
  Default to A (1 GPU) if the user doesn't specify or is unsure.

Confirm cluster is live:
```bash
ray status
```

**Starting the cluster (if not running):**
```bash
# Head node — temp-dir must be node-local (NOT a shared filesystem)
ray start --head --port=6379 --temp-dir=/tmp/$USER/ray --num-gpus=4

# Worker node — temp-dir flag is ignored on workers, they inherit from head
ray start --address=<head-ip>:6379 --num-gpus=4
```

**Important:** Do NOT use `--temp-dir` pointing to a shared filesystem.
Unix domain sockets (used for raylet communication) must be on node-local storage.
Using a shared filesystem causes `Could not connect to socket .../raylet.1` crashes.

If cluster shows correct number of GPUs, proceed.

## Step 4: Generate train.py

Generate `train.py` using the template in `references/train-template.md`.

Substitutions:
- `MODEL_CLASS` → class name from model file
- `MODEL_FILE` → import path (e.g., `from model import CNN`)
- `NUM_CLASSES` → from dataset
- `DATA_DIR` → confirmed path
- `NUM_WORKERS` → from cluster config

Place `train.py` in the same directory as the model file.

## Step 5: Dry Run

```bash
python train.py
```

Check:
- Exits with code 0
- Last line matches `val_acc=X.XXXX`
- No OOM errors (if OOM: reduce BATCH_SIZE or NUM_WORKERS)

Record the baseline `val_acc` value.

## Step 6: Confirm and Go

Show user:
```
Cluster:   {N} GPUs across {M} nodes
Model:     {model file} — {class name}
Dataset:   {dataset name}
GPU/task:  {0.5 (2 tasks/GPU, OOM→fallback to 1.0) | 1.0 (1 task/GPU)}
Baseline:  val_acc={value}
Scope:     {model file} (train.py is read-only boilerplate)
Verify:    python train.py
Mode:      sequential | parallel-{N}
```

Get confirmation, then start the loop.

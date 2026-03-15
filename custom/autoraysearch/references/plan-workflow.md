# Plan Workflow — /autoraysearch:plan

Convert a plain-language goal into a validated, ready-to-execute autoraysearch configuration.

**Output:** A confirmed setup (goal, model file, train.py, baseline val_acc) ready to launch the loop.

---

## Trigger

- User invokes `/autoraysearch:plan`
- User says "help me set up autoraysearch", "plan an autoraysearch run", "I want to iterate on my model"

---

## Phase 1: Capture Goal

Ask:

```
What do you want to improve? Describe in plain language.

Examples:
- "Improve forecast accuracy on my time-series model"
- "Reduce overfitting — val loss diverges from train loss"
- "Try attention mechanisms on my CNN"
- "Squeeze more R² out of this regression model"
```

If user provides goal text inline (e.g. `/autoraysearch:plan improve R²`), skip the question.

Record the goal. It will guide ideation in every loop iteration.

---

## Phase 2: Locate Model File

Ask:

```
Where is your model file? (the nn.Module subclass autoraysearch will modify)
```

Read the file fully. Confirm:
- Contains a class named `Model` (or ask to rename/wrap it)
- Has `__init__` and `forward` signatures
- `forward` input/output shapes are clear

If class is not named `Model`, offer to add an alias:
```python
Model = YourClassName  # added at bottom of file
```

---

## Phase 3: Locate or Generate train.py

Ask:

```
Do you already have a train.py that:
  1. Imports Model from model.py
  2. Trains on your data
  3. Prints val_acc=X.XXXX as the last stdout line

Options:
  A) Yes, I have one — tell me the path
  B) No — generate one from the template
```

**If A (existing train.py):**
- Read it. Confirm it prints `val_acc=X.XXXX` as last line.
- If it doesn't, ask: "What's the last line format? I'll adapt the extraction."
- Note the data paths, NUM_GPUS, and any config constants at the top.

**If B (generate):**
- Ask for: dataset type (CIFAR10 / CIFAR100 / custom numpy / custom DataLoader)
- Ask for: number of GPUs to use (default: 4)
- Ask for: data path (if custom)
- Ask:
  ```
  GPU allocation per experiment?
    A) 1 GPU per experiment (default — safest, up to 8 parallel on this cluster)
    B) 0.5 GPU per experiment — 2 experiments share one GPU (up to 16 parallel,
       auto-falls back to full GPU on OOM)
  ```
  Default is A if user does not respond or is unsure.
- Generate train.py from `references/train-template.md` using the chosen allocation
- Place it alongside model.py

---

## Phase 4: Dry Run

Run train.py to establish baseline:

```bash
python train.py
```

Check:
- Exit code 0
- Last stdout line matches `val_acc=X.XXXX`
- No OOM (if OOM: reduce BATCH_SIZE in train.py config section)

If it fails, fix the issue before proceeding. Do not start the loop on a broken baseline.

Record: `baseline val_acc = X.XXXX`

---

## Phase 5: Confirm & Launch

Present the configuration:

```
Goal:      {user's goal}
Model:     {model file path} — class Model
train.py:  {train.py path} (read-only)
Cluster:   {N} GPUs across {M} nodes
GPU/task:  {0.5 (2 tasks/GPU, OOM→fallback to 1.0) | 1.0 (1 task/GPU)}
Baseline:  val_acc={value}
Metric:    val_acc = (R² + IOA) / 2 — higher is better
Scope:     model.py only (train.py is never modified)
```

Ask:

```
How do you want to run?
  A) Sequential — one experiment per iteration (default)
  B) Parallel N — N experiments per iteration across the cluster
```

Then launch:
- Sequential → start `/autoraysearch` loop
- Parallel N → start `/autoraysearch --parallel N` loop

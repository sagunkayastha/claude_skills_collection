---
name: autoraysearch
description: Autonomous ML iteration on a Ray cluster. Generates train.py boilerplate from a model file and runs the autoresearch loop. User provides model.py; the skill handles Ray, DDP, dataset, and metric extraction.
version: 1.1.0
---

# autoraysearch — Ray-native Autonomous ML Research

Extends autoresearch with two key additions:
1. **Boilerplate generation** — user provides `model.py`, skill generates `train.py` (Ray + DDP)
2. **Parallel experiments** — optionally runs N experiments simultaneously across the cluster

## Environment

- Python: user's Python environment with Ray + PyTorch installed
- Ray cluster: multi-node, typically 2x4-GPU setup (8 GPUs total)

See `references/ray-cluster.md` for full cluster setup and known issues.

## File Structure

```
model.py    ← autoresearch scope (user's model, nn.Module subclass named "Model")
train.py    ← generated boilerplate, never modified by autoresearch
autoraysearch-results.tsv  ← results log (gitignored)
```

## Subcommands

| Subcommand | Purpose |
|------------|---------|
| `/autoraysearch` | Run the autonomous loop (sequential) |
| `/autoraysearch --parallel N` | Run N experiments simultaneously per iteration |
| `/autoraysearch:plan` | Interactive wizard: goal → model → train.py → baseline → launch |
| `/autoraysearch:setup` | Generate train.py from a model file (no goal wizard) |

## When to Activate

- User invokes `/autoraysearch` → run the loop (must already have baseline; if not, run plan first)
- User invokes `/autoraysearch:plan` → run the planning wizard
- User says "run autoresearch on the cluster", "use ray for the search loop", "iterate on my model with ray", "help me set up autoraysearch" → run the planning wizard
- User says "continue the loop", "keep iterating", "resume autoraysearch" → run the loop directly

## Planning Phase (/autoraysearch:plan)

Read `references/plan-workflow.md` for full protocol.

**Quick summary:**
1. Ask: what's your goal? (plain language)
2. Ask: where's your model file? Read it, confirm `Model` class exists.
3. Ask: existing train.py or generate one?
   - Existing: confirm it prints `val_acc=X.XXXX` as last line
   - Generate: ask dataset + GPU count, use `references/train-template.md`
4. Dry-run train.py → record baseline val_acc
5. Confirm config, ask sequential vs parallel, launch

## Setup Phase (legacy, no goal wizard)

Read `references/setup-protocol.md` for full details.

**If cluster is not running:**
```bash
# Head node
ray start --head --port=6379 --temp-dir=/tmp/$USER/ray --num-gpus=4
# Worker node
ray start --address=<head-ip>:6379 --num-gpus=4
```

## The Loop

Read `references/parallel-loop-protocol.md` for full details.

### Sequential mode (default)

```
LOOP:
  1. Review:  read model.py + git log + results log
  2. Ideate:  pick next atomic change to model.py
  3. Modify:  one change to model.py
  4. Commit:  git commit before verify
  5. Verify:  python train.py
  6. Extract: val_acc from last line of stdout
  7. Decide:  improved → keep | same/worse → git reset --hard HEAD~1
  8. Log:     append to autoraysearch-results.tsv
  9. Repeat:  NEVER STOP, NEVER ASK "should I continue?"
```

### Parallel mode (--parallel N)

Each iteration generates N candidate changes, applies them to N git branches,
submits N Ray jobs simultaneously, keeps the best. See `references/parallel-loop-protocol.md`.

## Critical Rules

1. **Scope is model.py only** — never modify train.py
2. **Model must export `Model`** — train.py imports this exact name
3. **One atomic change per iteration** — easy to attribute improvement
4. **Mechanical metric only** — val_acc from last stdout line, nothing subjective
5. **Auto-rollback** — git reset --hard HEAD~1 on any discard
6. **Git is memory** — read history before ideating
7. **Use the user's Python** — ask for it during setup if not already known

## What autoraysearch Can Tune in model.py

- Layer sizes (channels, hidden dims)
- Number of layers / depth
- Activation functions (ReLU → GELU → SiLU)
- Normalization (BatchNorm → LayerNorm → GroupNorm)
- Skip connections / residual blocks
- Dropout rates and placement
- Attention mechanisms
- Any architectural choice expressible in PyTorch

What it does NOT tune (those live in train.py config):
- LR, epochs, batch size, optimizer, scheduler — these can be tuned by editing train.py config section manually

## Results Log Format

```tsv
# metric_direction: higher_is_better
iteration  commit   metric   delta   status   description
0          baseline 0.8728   0.0     baseline initial state
1          a1b2c3d  0.8810   +0.008  keep     increase conv channels 64->128 in first block
2          -        0.8690   -0.004  discard  add extra ResBlock (underfits in 20 epochs)
```

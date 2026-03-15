# Parallel Loop Protocol — autoraysearch

Full protocol for parallel experiment execution. In parallel mode, each iteration
runs N experiments simultaneously on the Ray cluster instead of 1.

## Why Parallel?

ML training is expensive (minutes per run). Sequential search wastes cluster idle time.
Parallelism can be achieved two ways — choose based on model size:

### Option A: Fractional GPU (preferred for small models < ~5GB VRAM)

Set `num_gpus=0.5` in `train.py`. Ray schedules 2 tasks per GPU, 16 total on a 2×4 cluster.
No code changes needed beyond `NUM_GPUS = 0.5` and `torch.cuda.set_per_process_memory_fraction(0.45, 0)`.

| num_gpus | Tasks per GPU | Total (8-GPU cluster) | When to use |
|----------|---------------|----------------------|-------------|
| 0.5      | 2             | 16                   | Model < 5GB VRAM |
| 0.25     | 4             | 32                   | Model < 2GB VRAM |
| 1.0      | 1             | 8                    | Model > 10GB VRAM |

### Option B: Fractional workers per DDP job (for large models needing DDP)

With 8 GPUs and each job using 8 workers, you can only run 1 job at a time.
But with each job using 4 workers (1 node), you can run 2 jobs simultaneously.
With 2 workers each, you can run 4 jobs simultaneously (faster iteration, lower per-run accuracy).

| Cluster | Workers/job | Parallel jobs | Tradeoff |
|---------|-------------|---------------|---------|
| 2x4 GPU | 8 | 1 | Full cluster per job, most accurate |
| 2x4 GPU | 4 | 2 | Half cluster per job, 2x exploration |
| 2x4 GPU | 2 | 4 | Quarter cluster per job, 4x exploration |

Default: `--parallel 4` with 2 workers/job. User can override.

## Phase 1: Review

Same as autoresearch:
1. Read current model file
2. Read last 10-20 entries from results log (all branches)
3. Read `git log --oneline -20`
4. Identify patterns: what kinds of changes tend to work in this model?

## Phase 2: Ideate (Generate N Ideas)

Generate N distinct candidate changes in one pass. Rules:
- Each idea must be independent (no idea depends on another)
- Each idea must be testable in isolation
- Ideas should explore different directions (don't generate 4 variations of the same thing)
- Label them: `exp/1a`, `exp/1b`, `exp/1c`, `exp/1d`

Good idea diversity example (iteration 5):
- `exp/5a`: increase hidden dim 256 → 512
- `exp/5b`: replace MaxPool with strided conv
- `exp/5c`: add residual connections
- `exp/5d`: switch optimizer SGD → AdamW

Bad idea diversity (too similar):
- `exp/5a`: lr=0.01
- `exp/5b`: lr=0.005
- `exp/5c`: lr=0.001
- `exp/5d`: lr=0.0005

## Phase 3: Branch

For each idea, create a git branch:
```bash
git checkout -b exp/{iteration}{label}  # e.g., exp/5a
git checkout main  # back to main after each
```

Or use git worktrees for truly parallel filesystem access:
```bash
git worktree add /tmp/exp5a exp/5a
git worktree add /tmp/exp5b exp/5b
# ... apply changes to /tmp/exp5{a,b,...}/model.py
```

## Phase 4: Modify

Apply one change per branch. Each change must be atomic and describable in one sentence.

If using worktrees: edit `/tmp/exp5a/model.py`, `/tmp/exp5b/model.py`, etc.
If using branches: checkout each branch, edit, commit, return to main.

Commit each change:
```bash
git add model.py
git commit -m "experiment: {one-sentence description}"
```

## Phase 5: Submit Ray Jobs

Submit all N jobs simultaneously using `ray job submit`:

```bash
# Submit all jobs (non-blocking)
ray job submit --address=auto --working-dir=/tmp/exp5a \
  -- python train.py \
  > /tmp/ray_job_5a.log 2>&1 &

ray job submit --address=auto --working-dir=/tmp/exp5b \
  -- python train.py \
  > /tmp/ray_job_5b.log 2>&1 &

# Wait for all
wait
```

If not using worktrees (sequential branch checkout), fall back to submitting one at a time
and compare results at the end of the iteration.

## Phase 6: Wait and Collect

Poll until all jobs complete. Extract `val_acc` from each log:
```bash
grep "val_acc=" /tmp/ray_job_5a.log | tail -1
grep "val_acc=" /tmp/ray_job_5b.log | tail -1
```

Timeout: if any job exceeds 3x the average run time, treat as crash.

## Phase 7: Decide

Find the best result across all N experiments:

```
best = max(val_acc_5a, val_acc_5b, val_acc_5c, val_acc_5d)

IF best > current_best:
    Merge winning branch into main
    Delete all other experiment branches
    STATUS = "keep"
ELSE:
    Delete all experiment branches
    STATUS = "discard" (for all)
```

Merge the winner:
```bash
git checkout main
git merge exp/5a  # whichever won
git branch -d exp/5a exp/5b exp/5c exp/5d
```

## Phase 8: Log

Log all N experiments in results log, sharing the iteration number:

```tsv
5a  exp/5a  a1b2c3d  0.8750  +0.015  keep     increase hidden dim 256->512
5b  exp/5b  -        0.8580  -0.002  discard  replace MaxPool with strided conv
5c  exp/5c  -        0.8600  0.000   discard  add residual connections
5d  exp/5d  -        0.0000  0.000   crash    switch optimizer (OOM)
```

## Phase 9: Repeat

Go to Phase 1. Count each full parallel iteration as 1 toward any loop bound.

## When Stuck (>3 consecutive parallel iterations with no improvement)

1. Re-read ALL in-scope files from scratch
2. Look at the results log — are certain change types consistently failing?
3. Try more radical changes in the next iteration
4. Consider reducing parallelism and doing one careful experiment

## Sequential Fallback

If Ray cluster is unavailable or `ray status` fails, fall back to sequential mode
automatically. Log a warning. Sequential mode uses the same loop as autoresearch.

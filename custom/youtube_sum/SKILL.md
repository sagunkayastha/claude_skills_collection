---
name: youtube_sum
description: Use when the user wants to transcribe a YouTube video, get a transcript from a YouTube URL, convert YouTube audio to text, or summarize a YouTube video by first getting its transcript.
---

# YouTube Transcribe

Transcribe YouTube videos locally using faster-whisper (GPU-accelerated). Transcripts are saved as `.md` files named after the video title.

## Scripts

All scripts are in the `scripts/` folder relative to this skill:
- `scripts/transcribe.py` — full pipeline: download audio → transcribe with Whisper
- `scripts/get_transcript.py` — fast alternative using YouTube's built-in transcript API (no GPU)

**Python:** use the `pollen` conda env (defined in CLAUDE.md)

## Running as a Skill (Claude invokes this)

**Before running anything, ask the user these questions in a single message:**

> 1. **Timestamps** — every segment / every N seconds (how many?) / none?
> 2. **Format** — `.md` (default, works with Obsidian) or `.txt`?
> 3. **Model** — default is `large-v3-turbo` (~3GB VRAM, recommended). Change? Options: tiny / base / small / medium / large-v3-turbo / large-v3

Wait for the user's answers, then map them to script inputs and run:

```bash
printf "y\n1\n{ts_choice}\n{fmt_choice}\n{model_choice}\n" | $PYTHON scripts/transcribe.py "URL"
```

Prompt mapping:
- Confirm: always `y`
- Device: always `1` (local GPU)
- Timestamp: `1` = every segment, `2` + follow-up for interval, `3` = none
- Format: `1` = .md, `2` = .txt
- Model: `1`–`6` (large-v3-turbo = `5`)

After transcription completes:
1. Read the saved file
2. Fix obvious transcription errors (see Post-Processing below)
3. Save the corrected file
4. Tell the user what was fixed

## Quick Usage (user runs manually)

```bash
# Basic
python scripts/transcribe.py "https://youtube.com/watch?v=..."

# Plain text, no timestamps
python scripts/transcribe.py "URL" --no-timestamps

# Timestamp every 60 seconds
python scripts/transcribe.py "URL" --timestamp-interval 60

# Force language
python scripts/transcribe.py "URL" --language en

# Keep the downloaded audio
python scripts/transcribe.py "URL" --keep-audio
```

## Interactive Prompts (in order)

1. Shows video title, channel, duration — asks to confirm
2. Device: `[1]` Local GPU (default) · `[2]` Vast.ai
3. Timestamp mode: `[1]` Every segment · `[2]` Every N seconds · `[3]` None
4. Output format: `[1]` `.md` (default, Obsidian-friendly) · `[2]` `.txt`
5. Model selection (see below)

## Model Options (RTX 3060 Mobile, 6GB VRAM)

| # | Model | VRAM |
|---|---|---|
| 1 | tiny | ~0.5 GB |
| 2 | base | ~1 GB |
| 3 | small | ~2 GB |
| 4 | medium | ~4 GB |
| **5** | **large-v3-turbo** | **~3 GB** ← default |
| 6 | large-v3 | ~6 GB (tight) |

## Output

Transcripts saved as `<video title>.md` in the skill root directory.
Model cache: `~/.cache/huggingface/hub/` (downloads once, reused after)

## Alternative: YouTube Auto-Transcript (no GPU)

Try this first — much faster, no download needed:

```bash
python scripts/get_transcript.py "URL"
```

Falls back to `transcribe.py` if no transcript is available on YouTube.

## Post-Processing (when run as a skill)

After transcription, **always read and fix obvious errors** before reporting done:

- AI/tech names: "cloud code" → "Claude Code", "CLAUDE.md" not "cloud.md", model names, brand names
- Homophones wrong in context
- Garbled proper nouns (people, products, companies)
- "brain dubs" → "brain dumps", "rebos" → "repos", etc.

Do NOT rephrase or change meaning — only fix clear transcription errors.
Briefly tell the user what was corrected.

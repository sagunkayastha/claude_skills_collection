---
name: notify
description: Use when the user says "notify me", "send me a message", "ping my phone", "alert me when done", or when a long-running task completes and the user should be informed.
---

# Notify

Send a one-way Telegram notification to the user's phone.

## Command

```bash
python ~/.claude/tools/notify.py "your message here"
```

The script prepends the machine hostname automatically: `[hostname] your message here`

If no message is given, it sends `"Done."` by default.

## Setup (one-time)

1. Place `notify.py` at `~/.claude/tools/notify.py`
2. Create `~/.claude/tools/telegram.env` with:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

Do **not** paste tokens in chat — edit the file directly.

## When to Use

- User says "notify me when done" → run notify at the end of the task
- Long-running Bash command → chain notify after it
- User explicitly asks to send a message to their phone

## Example

```bash
# After a long build
python ~/.claude/tools/notify.py "Build complete"
```

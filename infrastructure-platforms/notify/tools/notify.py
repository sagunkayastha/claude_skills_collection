"""Send a one-way Telegram notification."""

import sys
import os
import socket
import urllib.request
import urllib.parse
import json
from pathlib import Path

env_file = Path(__file__).parent / "telegram.env"
config = {}
for line in env_file.read_text().splitlines():
    if "=" in line and not line.startswith("#"):
        k, v = line.split("=", 1)
        config[k.strip()] = v.strip()

TOKEN = config["TELEGRAM_BOT_TOKEN"]
CHAT_ID = config["TELEGRAM_CHAT_ID"]

host = socket.gethostname()
body = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Done."
message = f"[{host}] {body}"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = urllib.parse.urlencode({"chat_id": CHAT_ID, "text": message}).encode()
req = urllib.request.Request(url, data=data)
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
    if result.get("ok"):
        print("Notification sent.")
    else:
        print(f"Failed: {result}", file=sys.stderr)
        sys.exit(1)

import argparse
import json
import os
import subprocess
import sys
import tempfile

# Ensure conda env bin is in the DLL search path so ctranslate2 can find CUDA DLLs
if hasattr(os, "add_dll_directory"):
    _env_bin = os.path.dirname(sys.executable)
    os.add_dll_directory(_env_bin)


MODELS = {
    "1": ("tiny",           "~0.5 GB"),
    "2": ("base",           "~1 GB"),
    "3": ("small",          "~2 GB"),
    "4": ("medium",         "~4 GB"),
    "5": ("large-v3-turbo", "~3 GB  [recommended for 6GB GPU]"),
    "6": ("large-v3",       "~6 GB  [tight on 6GB GPU]"),
}


def get_metadata(url: str) -> dict:
    result = subprocess.run(
        [sys.executable, "-m", "yt_dlp", "--dump-json", "--no-playlist", url],
        capture_output=True, text=True, check=True,
    )
    data = json.loads(result.stdout)
    duration_s = data.get("duration", 0)
    minutes, seconds = divmod(int(duration_s), 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        duration_str = f"{hours}h {minutes}m {seconds}s"
    else:
        duration_str = f"{minutes}m {seconds}s"
    return {
        "title": data.get("title", "Unknown"),
        "duration": duration_str,
        "channel": data.get("channel") or data.get("uploader", "Unknown"),
    }


def ask(prompt: str, default: str = "") -> str:
    val = input(prompt).strip()
    return val if val else default


def choose_model() -> tuple[str, str]:
    print("\nChoose model:")
    for key, (name, vram) in MODELS.items():
        print(f"  [{key}] {name:<20} VRAM: {vram}")
    choice = ask("\nModel [5]: ", "5")
    if choice not in MODELS:
        print("Invalid choice, using default (large-v3-turbo)")
        choice = "5"
    model_name, vram = MODELS[choice]
    print(f"  -> {model_name} ({vram})")
    return model_name, vram


def choose_device() -> tuple[str, str]:
    print("\nWhere to run?")
    print("  [1] Local GPU (default)")
    print("  [2] Vast.ai server")
    choice = ask("\nDevice [1]: ", "1")
    if choice == "2":
        return "vastai", ""
    return "local", "cuda"


def download_audio(url: str, out_path: str):
    print("\nDownloading audio...")
    subprocess.run(
        [
            sys.executable, "-m", "yt_dlp",
            "-x", "--audio-format", "mp3",
            "-o", out_path,
            "--no-playlist",
            url,
        ],
        check=True,
    )


def transcribe_local(audio_path: str, model_name: str, language: str | None,
                     no_timestamps: bool, timestamp_interval: float | None) -> list[str]:
    from faster_whisper import WhisperModel

    print(f"\nLoading model '{model_name}' on CUDA (int8_float16)...")
    model = WhisperModel(model_name, device="cuda", compute_type="int8_float16")

    print("Transcribing...")
    segments, info = model.transcribe(audio_path, beam_size=5, language=language)

    print(f"Detected language: {info.language} (probability: {info.language_probability:.2f})\n")

    lines = []
    last_timestamp = -1e9
    for segment in segments:
        text = segment.text.strip()
        if no_timestamps:
            line = text
        elif timestamp_interval is not None:
            if segment.start - last_timestamp >= timestamp_interval:
                mins, secs = divmod(int(segment.start), 60)
                lines.append(f"\n[{mins:02d}:{secs:02d}]")
                last_timestamp = segment.start
            line = text
        else:
            line = f"[{segment.start:.1f}s -> {segment.end:.1f}s] {text}"
        print(line)
        lines.append(line)

    return lines


def parse_args():
    parser = argparse.ArgumentParser(
        description="Download and transcribe a YouTube video using faster-whisper."
    )
    parser.add_argument("url", help="YouTube URL or video ID")
    parser.add_argument("-o", "--output", default=None, help="Output transcript file path")
    parser.add_argument("--language", default=None, help="Force language (e.g. 'en')")
    parser.add_argument("--no-timestamps", action="store_true", help="Plain text output")
    parser.add_argument("--timestamp-interval", type=float, default=None,
                        metavar="SECONDS", help="Add timestamp every N seconds (e.g. 60)")
    parser.add_argument("--keep-audio", action="store_true", help="Keep downloaded audio")
    parser.add_argument("--audio-out", default=None, help="Path to save audio (with --keep-audio)")
    return parser.parse_args()


def main():
    args = parse_args()

    # Step 1: Fetch and show metadata
    print("Fetching video info...")
    try:
        meta = get_metadata(args.url)
    except Exception as e:
        print(f"Could not fetch metadata: {e}")
        sys.exit(1)

    print(f"\n  Title:    {meta['title']}")
    print(f"  Channel:  {meta['channel']}")
    print(f"  Duration: {meta['duration']}")

    confirm = ask("\nTranscribe this video? [Y/n]: ", "y").lower()
    if confirm not in ("y", "yes", ""):
        print("Aborted.")
        sys.exit(0)

    # Step 2: Choose device
    device_choice, device = choose_device()

    if device_choice == "vastai":
        print("\nVast.ai support not yet implemented. Falling back to local GPU.")
        device = "cuda"

    # Step 3: Choose timestamp mode (only if not set via CLI)
    timestamp_interval = args.timestamp_interval
    no_timestamps = args.no_timestamps
    if not no_timestamps and timestamp_interval is None:
        print("\nTimestamp mode:")
        print("  [1] Every segment (default)")
        print("  [2] Every N seconds")
        print("  [3] None (plain text)")
        ts_choice = ask("\nChoice [1]: ", "1")
        if ts_choice == "2":
            val = ask("  Interval in seconds [60]: ", "60")
            try:
                timestamp_interval = float(val)
            except ValueError:
                timestamp_interval = 60.0
        elif ts_choice == "3":
            no_timestamps = True

    # Step 4: Choose output format
    if args.output:
        ext = os.path.splitext(args.output)[1] or ".md"
    else:
        print("\nOutput format:")
        print("  [1] Markdown .md (default, works with Obsidian)")
        print("  [2] Plain text .txt")
        fmt_choice = ask("\nChoice [1]: ", "1")
        ext = ".txt" if fmt_choice == "2" else ".md"

    # Step 5: Choose model
    model_name, _ = choose_model()

    # Step 6: Download + transcribe
    skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    safe_title = "".join(c if c.isalnum() or c in " -_()" else "_" for c in meta["title"]).strip()
    output_path = args.output or os.path.join(skill_dir, f"{safe_title}{ext}")

    if args.keep_audio:
        audio_path = args.audio_out or os.path.join(skill_dir, "audio.mp3")
        download_audio(args.url, audio_path)
        lines = transcribe_local(audio_path, model_name, args.language, no_timestamps, timestamp_interval)
    else:
        with tempfile.TemporaryDirectory() as tmp:
            audio_path = os.path.join(tmp, "audio.mp3")
            download_audio(args.url, audio_path)
            lines = transcribe_local(audio_path, model_name, args.language, no_timestamps, timestamp_interval)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"\nTranscript saved to: {output_path}")


if __name__ == "__main__":
    main()

import sys
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(url_or_id: str) -> str:
    # Extract video ID from URL or use as-is
    if "youtube.com" in url_or_id or "youtu.be" in url_or_id:
        import re
        match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url_or_id)
        if not match:
            raise ValueError("Could not extract video ID from URL")
        video_id = match.group(1)
    else:
        video_id = url_or_id

    transcript = YouTubeTranscriptApi().fetch(video_id)
    return " ".join(t.text for t in transcript)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_transcript.py <youtube_url_or_id>")
        sys.exit(1)

    text = get_transcript(sys.argv[1])
    print(text)

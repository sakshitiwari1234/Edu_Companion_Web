import sys
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        lines = [entry['text'] for entry in transcript]
        return lines
    except TranscriptsDisabled:
        print("❌ Transcripts are disabled for this video.")
    except NoTranscriptFound:
        print("❌ No transcript available for this video.")
    except Exception as e:
        print("❌ Unexpected error:", str(e))
    return []

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Please provide a YouTube video ID.")
        sys.exit(1)

    video_id = sys.argv[1]
    result = get_transcript(video_id)
    for line in result:
        print(line)

from youtube_transcript_api import YoutubeTranscriptApi
from utils.video_utils import extract_video_id

def get_transcript(video_url):
    """
    Fetches the transcript of a YouTube video.
    """
    try:
        video_id = extract_video_id(video_url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([entry["text"] for entry in transcript])
        return text
    except Exception as e:
        raise Exception(f"Error fetching video transcript: {e}")
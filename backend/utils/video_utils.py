import re

def extract_video_id(video_url):
    """
    Extract the video ID from a YouTube URL.
    """
    try:
        # Regex to match YouTube video IDs
        pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
        match = re.search(pattern, video_url)
        if match:
            return match.group(1)
        else:
            raise ValueError("Invalid YouTube URL")
    except Exception as e:
        raise Exception(f"Error extracting video ID: {e}")
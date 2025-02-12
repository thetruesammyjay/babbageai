import pytest
from services.video_service import get_transcript

def test_get_transcript():
    # Test with a sample YouTube video URL
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    transcript = get_transcript(video_url)
    assert isinstance(transcript, str)
    assert len(transcript) > 0
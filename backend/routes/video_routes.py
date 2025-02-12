from fastapi import APIRouter, HTTPException
from services.video_service import get_transcript
from services.deepseek_service import ask_deepseek

router = APIRouter()

@router.post("/video/process")
async def process_video(video_url: str):
    try:
        # Fetch the transcript
        transcript = get_transcript(video_url)

        return {"transcript": transcript}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    # DeepSeek API configuration
    DEEPSEEK_API_URL = os.getenv("DEEPSEEK_API_URL", "https://api.deepseek.com/v1/answer")
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "your_deepseek_api_key")

    # File storage paths
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "storage")
    DOCUMENTS_FOLDER = os.path.join(UPLOAD_FOLDER, "documents")
    IMAGES_FOLDER = os.path.join(UPLOAD_FOLDER, "images")
    TRANSCRIPTS_FOLDER = os.path.join(UPLOAD_FOLDER, "transcripts")

    # Ensure upload folders exist
    for folder in [UPLOAD_FOLDER, DOCUMENTS_FOLDER, IMAGES_FOLDER, TRANSCRIPTS_FOLDER]:
        os.makedirs(folder, exist_ok=True)

settings = Settings()
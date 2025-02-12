from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.ocr_routes import router as ocr_router
from routes.document_routes import router as document_router
from routes.video_routes import router as video_router
from routes.auth_routes import router as auth_router
from config.settings import settings

# Initialize the FastAPI app
app = FastAPI(title="BabbageAI", version="1.0.0")

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all origins (update for production)
    allow_credentials=True,
    allow_methods=["*"], # Allow all HTTP methods
    allow_headers=["*"], # Allow all headers
)

# Include all routes
app.include_router(ocr_router, prefix="/api/ocr", tags=["OCR"])
app.include_router(document_router, prefix="/api/document", tags=["Document"])
app.include_router(video_router, prefix="/api/video", tags=["Video"])
app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to BabbageAI!"}
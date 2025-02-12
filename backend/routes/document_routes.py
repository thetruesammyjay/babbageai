from fastapi import APIRouter, File, UploadFile, HTTPException
from services.document_service import extract_text_from_pdf, extract_text_from_docx
from services.deepseek_service import ask_deepseek
from utils.file_utils import save_uploaded_file

router = APIRouter()

@router.post("/document/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        # Save the uploaded file
        file_path = save_uploaded_file(file, "storage/documents")

        # Extract text based on file
        if file.filename.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif file.filename.endswith(".docx"):
            text = extract_text_from_docx(file_path)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")
        
        return {"text": text}
    except Exception as e:
        raise HTTPException(staus_code=500, detail=str(e))
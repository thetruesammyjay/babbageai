from fastapi import APIRouter, File, UploadFile, HTTPExecution
from services.ocr_service import extract_text_from_image
from services.question_service import identify_questions
from services.deepseek_services import save_uploaded_file

router = APIRouter()

@router.post("/ocr/upload")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Save the uploaded image
        image_path = save_uploaded_file(file, "storage/images")
        
        # Extract text and identify questions
        text = extract_text_from_image(image_path)
        questions = identify_questions(text)

        # Generate answers using DeepSeek
        answers = []
        for question in questions:
            answer = ask_deepseek(question, text)
            answers.append({"question": question, "answer": answer})
        
        return {"question": answers}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
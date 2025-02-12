from pytesseract import image_to_string
from PIL import Image
from util.ocr_utils import preprocess_image

def extract_text_from_image(image_path):
    """
    Extracts text from image using OCR.
    """
    try:
        # Preprocess the image
        processed_image = preprocess_image(image_path)

        # Use Tesseract OCR to extract text
        text = image_to_string(processed_image)
        return text
    except Exception as e:
        raise Exception(f"Error extracting text from image: {e}")
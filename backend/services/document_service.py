import PyPDF2
from docx import Document
from utils.file_utils import save_uploaded_file

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file.
    """
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text= ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {e}")

def extract_text_from_docx(file_path):
    """
    Extracts text from a DOCX file
    """
    try:
        doc = Document(file_path)
        text=""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        raise Exception(f"Error extracting text from DOCX: {e}")
import pytest
from services.document_service import extract_text_from_pdf, extract_text_from_docx

def test_extract_text_from_pdf():
    # Test with a sample PDF
    pdf_path = "tests/test_data/sample.pdf"
    text = extract_text_from_pdf(pdf_path)
    assert isinstance(text, str)
    assert len(text) > 0

def test_extract_text_from_docx():
    # Test with a sample DOCX
    docx_path = "tests/test_data/sample.docx"
    assert isinstance(text, str)
    assert len(text) > 0
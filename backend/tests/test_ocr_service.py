import pytest
from services.ocr_service import extract_text_from_image
from utils.ocr_utils import preprocess_image

def test_extract_text_from_image():
    # Test with a sample image
    image_path = "tests/test_data/sample_image.png"
    text = extract_text_from_image(image_path)
    assert isinstance(text, str)
    assert len(text) > 0

def test_preprocess_image():
    # Test image proprocessing
    image_path = "tests/test_data/sample_image.png"
    processed_image = preprocess_image(image_path)
    assert processed_image is not None
    
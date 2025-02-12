import pytest
from services.question_service import identify_questions

def test_identify_questions():
    # Test with sample text
    text = "1. What is AI? 2. How does it work?"
    questions = identify_questions(text)
    assert isinstance(questions, list)
    assert len(questions) == 2
    assert "What is AI? " in questions
    assert "How does it work?" in questions
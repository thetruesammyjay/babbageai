import pytest
from services.deepseek_service import ask_deepseek

def test_ask_deepseek():
    # Test with a sample question and context
    question = "What is AI?"
    context = "Artificial Intelligence (AI) is the simulation of human intelligence in machines."
    answer = ask_deepseek(question, context)
    assert isinstance(answer, str)
    assert len(answer) > 0
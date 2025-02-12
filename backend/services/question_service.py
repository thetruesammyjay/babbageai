import re

def identify_questions(text):
    """
    Identifies question from extracted text using regex.
    """
    try:
        # Regex to match questions
        questions = re.findall(r'\d+\..*?\?|What.*?\?|How.*?\?', text)
        return questions
    except Exception as e:
        raise Exception(f"Error identifying questions: {e}")
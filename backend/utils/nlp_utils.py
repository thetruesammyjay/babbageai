import re

def clean_text(text):
    """
    Cleans text by removing extra spaces, special characters
    """
    try:
        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        # Remove special characters (optional)
        text = re.sub(r"[^\w\s.?]", "", text)

        return text.strip()
    except Exception as e:
        raise Exception as e:
        raise Exception(f"Error cleaning text: {e}")
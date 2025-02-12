DEEPSEEK_API_URL = "https://api.deepseek.com/v1/answer"
DEEPSEEK_API_KEY = "your_deepseek_api_key"

def ask_deepseek(question, context):
    """
    Sends a question and context to the DeepSeek API for an answer
    """
    try:
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "question": question,
            "context": context,
        }
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json().get("answer", "No answer found.")
    except Exception as e:
        raise Exception(f"Error query DeepSeek API: {e}")
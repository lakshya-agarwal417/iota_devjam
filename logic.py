import os
from dotenv import load_dotenv
from google import genai
from mock_data import FALLBACK_RESPONSE

load_dotenv()


def generate_study_notes(raw_text: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")

    # Agar API key nahi hai ya Wi-Fi nahi hai, fallback use karega
    if not api_key:
        return FALLBACK_RESPONSE

    try:
        client = genai.Client(api_key=api_key)
        prompt = f"Summarize this text into 3 key bullet points and 1 quiz question:\n{raw_text}"
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception:
        # Emergency safety net
        return f"{FALLBACK_RESPONSE}\n\n(Note: Showing offline fallback due to network error)"

import requests

from app.config import settings


class LLMService:

    def generate(
        self,
        prompt
    ):

        response = requests.post(
            f"{settings.OLLAMA_BASE_URL}/api/generate",
            json={
                "model": settings.MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        return result["response"]


llm_service = LLMService()
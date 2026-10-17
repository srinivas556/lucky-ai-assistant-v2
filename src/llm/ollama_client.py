import requests
from config import MODEL, OLLAMA_BASE_URL

class OllamaClient:
    def __init__(self, model=MODEL, base_url=OLLAMA_BASE_URL):
        self.model = model
        self.base_url = base_url.rstrip("/")

    def chat(self, messages):
        response = requests.post(
            f"{self.base_url}/api/chat",
            json={"model": self.model, "messages": messages, "stream": False},
            timeout=120,
        )
        response.raise_for_status()
        return response.json()["message"]["content"]

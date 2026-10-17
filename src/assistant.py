from pathlib import Path
from llm.ollama_client import OllamaClient

class JarvisAssistant:
    def __init__(self):
        self.client = OllamaClient()
        prompt_path = Path(__file__).parent / "prompts" / "system_prompt.txt"
        self.system_prompt = prompt_path.read_text(encoding="utf-8")

    def respond(self, user_text):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_text},
        ]
        return self.client.chat(messages)

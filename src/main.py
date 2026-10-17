import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from assistant import JarvisAssistant

def main():
    assistant = JarvisAssistant()
    print("JARVIS v0.1 — Local AI Assistant")
    print("Type 'exit' to quit. Make sure Ollama is running.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nJARVIS: Goodbye.")
            break

        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            print("JARVIS: Goodbye.")
            break

        try:
            answer = assistant.respond(user_input)
            print(f"JARVIS: {answer}\n")
        except Exception as exc:
            print(f"JARVIS: I could not complete that request.\nError: {exc}\n")

if __name__ == "__main__":
    main()

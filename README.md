# 🤖 Lucky v0.2.0 — Local AI Assistant

**A privacy-focused personal AI assistant powered by Python and Ollama.**

Lucky is a local AI assistant project exploring LLM integration, prompt engineering, conversational AI, and voice interaction.

## ✨ Features

- Local AI responses using Ollama
- Browser-based chat interface
- FastAPI backend for chat requests
- Conversation history support
- Configurable Ollama model
- Voice-assistant development roadmap

## 🛠️ Tech Stack

- Python
- FastAPI
- Ollama
- Qwen3
- HTML, CSS, JavaScript

## 📋 Prerequisites

- Python installed
- [Ollama](https://ollama.com/) installed and running
- A supported Ollama model downloaded, such as `qwen3:4b`

Pull the model if necessary:

```bash
ollama pull qwen3:4b
```

## 🚀 Run Lucky Locally

### 1. Clone the repository

```bash
git clone https://github.com/srinivas556/lucky-local-ai-assistant.git
cd lucky-local-ai-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the API

In the project root, run:

```bash
python -m uvicorn api:app --host 127.0.0.1 --port 8001
```

Keep this terminal running.

### 5. Start the website

Open a second terminal in the project root and run:

```bash
python -m http.server 8000 --directory docs
```

Open **http://127.0.0.1:8000/** in your browser.

Both the API and website must be running for chat to work.

## ⚙️ Configuration

The API defaults to `qwen3:4b` and `http://localhost:11434` for Ollama.

You can override these settings using environment variables:

- `JARVIS_MODEL`
- `OLLAMA_BASE_URL`

The API reads its system prompt from `src/prompts/system_prompt.txt`.

## 🗺️ Roadmap

- **v0.1.0:** Text-based command-line assistant
- **v0.2.0:** Browser chat and FastAPI integration
- **v0.3.0:** Voice integration
- **v0.4.0:** Improved coding assistance, reliability, and response handling

## 🔒 Privacy and Safety

The browser interface and API are configured for local development. Do not expose the API or Ollama service directly to the public internet. A public deployment requires an appropriately secured, reachable backend.

Never commit `.env` files, API keys, passwords, or other secrets.

## 👨‍💻 Author

**Srinivas**

GitHub: [@srinivas556](https://github.com/srinivas556)

---

*Building my own AI assistant, one prompt at a time.*s
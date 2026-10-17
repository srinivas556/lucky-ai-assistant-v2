
import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

load_dotenv()

app = FastAPI(title="Lucky AI Chat API")

# Read the secret from an environment variable.
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.1-8b-instant",
)

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

PROMPT_FILE = (
    Path(__file__).resolve().parent
    / "src"
    / "prompts"
    / "system_prompt.txt"
)

# Local frontend origins for development.
allowed_origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

# Add the deployed frontend origin through configuration later.
frontend_origin = os.getenv("FRONTEND_ORIGIN", "").strip()
if frontend_origin:
    allowed_origins.append(frontend_origin)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)
    history: list[dict] = Field(default_factory=list, max_length=10)


@app.get("/")
def health():
    return {"status": "ok", "assistant": "Lucky"}


@app.post("/api/chat")
def chat(body: ChatRequest):
    message = body.message.strip()

    if not message:
        raise HTTPException(
            status_code=400,
            detail="Please enter a message.",
        )

    if not GROQ_API_KEY:
        raise HTTPException(
            status_code=503,
            detail="Online AI is not configured. Set GROQ_API_KEY.",
        )

    if not PROMPT_FILE.is_file():
        raise HTTPException(
            status_code=500,
            detail="System prompt file is missing.",
        )

    system_prompt = PROMPT_FILE.read_text(
        encoding="utf-8"
    ).strip()

    system_prompt += (
        "\n\nAnswer naturally, directly, and concisely. "
        "For greetings, use one short sentence. "
        "Do not include internal reasoning or deliberation. "
        "Give explanations only when the user asks for them."
    )

    messages = [
        {"role": "system", "content": system_prompt}
    ]

    for item in body.history[-10:]:
        if (
            not isinstance(item, dict)
            or item.get("role") not in {"user", "assistant"}
            or not isinstance(item.get("content"), str)
            or len(item["content"]) > 4000
        ):
            raise HTTPException(
                status_code=400,
                detail="Invalid chat history.",
            )

        messages.append({
            "role": item["role"],
            "content": item["content"],
        })

    messages.append({
        "role": "user",
        "content": message,
    })

    try:
        response = requests.post(
            GROQ_URL,
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": GROQ_MODEL,
                "messages": messages,
                "temperature": 0.5,
                "max_tokens": 300,
                "stream": False,
            },
            timeout=60,
        )

        if response.status_code == 429:
            raise HTTPException(
                status_code=429,
                detail="AI usage limit reached. Please try again later.",
            )

        if response.status_code in (401, 403):
            raise HTTPException(
                status_code=503,
                detail="AI authentication failed. Check the server API key.",
            )

        response.raise_for_status()

        data = response.json()
        reply = data["choices"][0]["message"]["content"].strip()

        if not reply:
            raise HTTPException(
                status_code=502,
                detail="Lucky returned an empty response.",
            )

        return {
            "reply": reply,
            "model": GROQ_MODEL,
        }

    except HTTPException:
        raise

    except requests.Timeout:
        raise HTTPException(
            status_code=504,
            detail="Lucky took too long to respond.",
        )

    except requests.RequestException as exc:
        print("Groq API error:", str(exc))
        if getattr(exc, "response", None) is not None:
            print("Groq response:", exc.response.text[:1000])
        raise HTTPException(
            status_code=502,
            detail="The online AI service returned an error.",
        )

    except (KeyError, IndexError, TypeError, ValueError):
        raise HTTPException(
            status_code=502,
            detail="Invalid response from the online AI service.",
        )

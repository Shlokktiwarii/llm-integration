import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".env")


LLM_ENABLED = os.getenv(
    "LLM_ENABLED",
    "true",
).lower() == "true"


client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
    timeout=float(os.getenv("LLM_TIMEOUT", "60")),
)


def call_llm(prompt: str) -> str:

    if not LLM_ENABLED:
        raise RuntimeError(
            "LLM service is currently disabled"
        )

    response = client.chat.completions.create(
        model=os.getenv("LLM_MODEL"),
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0,
    )

    content = response.choices[0].message.content

    if not content:
        raise RuntimeError(
            "LLM returned an empty response"
        )

    return content.strip()
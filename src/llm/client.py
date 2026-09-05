import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


# Finding project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Loading .env from project root
load_dotenv(BASE_DIR / ".env")


client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
)


def call_llm(prompt: str) -> str:
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

    return response.choices[0].message.content
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

PROMPT_PATH = (
    BASE_DIR
    / "prompt"
    / "v1.txt"
)


def load_resume_prompt(text: str) -> str:
    prompt_template = PROMPT_PATH.read_text(
        encoding="utf-8"
    )

    return prompt_template.replace("{text}", text)
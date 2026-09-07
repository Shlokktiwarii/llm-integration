from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

PROMPTS_DIR = BASE_DIR / "prompt"
RESUME_PROMPT_PATH = PROMPTS_DIR / "v1.txt"
REPAIR_PROMPT_PATH = PROMPTS_DIR / "repair_v1.txt"


def load_resume_prompt(text: str) -> str:
    prompt_template = RESUME_PROMPT_PATH.read_text(
        encoding="utf-8"
    )
    return prompt_template.replace("{text}", text)


def load_repair_prompt(invalid_response: str) -> str:
    prompt_template = REPAIR_PROMPT_PATH.read_text(
        encoding="utf-8"
    )

    return prompt_template.replace("{invalid_response}", invalid_response)

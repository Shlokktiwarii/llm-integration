from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

QUARANTINE_DIR = (
    BASE_DIR
    / "logs"
    / "quarantine"
)

QUARANTINE_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


def quarantine_response(
    original_text: str,
    raw_response: str,
    error: str,
):
    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    file_path = (
        QUARANTINE_DIR
        / f"failed_{timestamp}.txt"
    )

    content = f"""
TIMESTAMP:
{timestamp}

ERROR:
{error}

ORIGINAL INPUT:
{original_text}

RAW LLM RESPONSE:
{raw_response}
"""

    file_path.write_text(
        content.strip(),
        encoding="utf-8",
    )
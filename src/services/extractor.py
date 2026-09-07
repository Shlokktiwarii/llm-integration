import json

from pydantic import ValidationError
from src.utils.json_parser import parse_llm_json
from src.llm.client import call_llm
from src.prompts.loader import load_resume_prompt, load_repair_prompt
from src.schemas.resume import ResumeExtraction
from src.utils.quarantine import quarantine_response


def parse_and_validate(raw_response: str) -> ResumeExtraction:
    data = parse_llm_json(raw_response)
    return ResumeExtraction.model_validate(data)

def extract_resume(text: str) -> ResumeExtraction:
    # LLM Attempt
    prompt = load_resume_prompt(text)

    raw_response = call_llm(prompt)

    print("\n========== FIRST LLM RESPONSE ==========")
    print(raw_response)
    print("========================================")

    try:
        return parse_and_validate(raw_response)

    except (
        json.JSONDecodeError,
        ValidationError,
    ) as first_error:

        print("\nFirst attempt failed.")
        print(first_error)

    # Repair Attempt

    repair_prompt = load_repair_prompt(
        raw_response
    )

    repaired_response = call_llm(
        repair_prompt
    )

    print("\n========== REPAIRED RESPONSE ==========")
    print(repaired_response)
    print("=======================================")

    try:
        return parse_and_validate(
            repaired_response
        )

    except (
        json.JSONDecodeError,
        ValidationError,
    ) as repair_error:

        # -------------------------
        # Quarantine
        # -------------------------

        quarantine_response(
            original_text=text,
            raw_response=repaired_response,
            error=str(repair_error),
        )

        raise ValueError(
            "LLM output failed validation "
            "after repair attempt."
        )
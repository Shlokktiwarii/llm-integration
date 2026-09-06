import json

from pydantic import ValidationError
from src.utils.json_parsor import parse_llm_json
from src.llm.client import call_llm
from src.prompts.loader import load_resume_prompt
from src.schemas.resume import ResumeExtraction


def extract_resume(text: str) -> ResumeExtraction:

    # 1. Load prompt
    prompt = load_resume_prompt(text)

    # 2. Call LLM
    raw_response = call_llm(prompt)

    # Debug for now
    print("\nRAW LLM RESPONSE:")
    print(raw_response)

    # 3. Parse JSON
    try:
        data = parse_llm_json(raw_response)

    except json.JSONDecodeError as error:
        raise ValueError(
            f"LLM returned invalid JSON: {error}"
        )

    # 4. Validate schema
    try:
        validated_output = ResumeExtraction.model_validate(data)

    except ValidationError as error:
        raise ValueError(
            f"LLM returned invalid schema: {error}"
        )

    return validated_output
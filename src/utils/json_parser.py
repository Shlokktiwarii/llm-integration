import json
import re


def parse_llm_json(raw_response: str) -> dict:
    """
    Extract and parse JSON from an LLM response.
    Handles markdown code fences and extra text.
    """

    cleaned = raw_response.strip()

    # Remove opening markdown fence
    cleaned = re.sub(
        r"^```(?:json)?\s*",
        "",
        cleaned,
        flags=re.IGNORECASE,
    )

    # Remove closing markdown fence
    cleaned = re.sub(
        r"\s*```$",
        "",
        cleaned,
    )

    cleaned = cleaned.strip()

    # Find the JSON object
    start = cleaned.find("{")
    end = cleaned.rfind("}")

    if start == -1 or end == -1:
        raise json.JSONDecodeError(
            "No JSON object found",
            cleaned,
            0,
        )

    json_string = cleaned[start:end + 1]

    return json.loads(json_string)
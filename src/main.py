import os

from fastapi import FastAPI, HTTPException

from src.schemas.resume import ExtractionResponse, ResumeRequest
from src.services.extractor import extract_resume


app = FastAPI(
    title="AI Resume & Job Profile Extractor",
    version="0.1.0",
)


@app.get("/")
def health_check():

    llm_enabled = os.getenv(
        "LLM_ENABLED",
        "true",
    ).lower() == "true"
    return {
        "status": "healthy",
        "service": "AI Resume Extractor",
        "llm_enabled": llm_enabled,
    }


@app.post(
    "/extract",
    response_model=ExtractionResponse,
)
def extract_resume_endpoint(request: ResumeRequest):

    try:
        result, latency = extract_resume(request.text)

        return {
            "data": result,
            "metadata": {
                "latency_seconds": round(latency, 2),
                "model": os.getenv("LLM_MODEL") or "unknown",
            },
        }

    except ValueError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error),
        )

    except RuntimeError as error:
        raise HTTPException(
            status_code=503,
            detail=str(error),
        )
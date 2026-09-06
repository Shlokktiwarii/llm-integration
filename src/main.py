from fastapi import FastAPI, HTTPException

from src.schemas.resume import ResumeRequest, ResumeExtraction
from src.services.extractor import extract_resume


app = FastAPI(
    title="AI Resume & Job Profile Extractor",
    version="0.1.0",
)


@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Resume Extractor",
    }


@app.post(
    "/extract",
    response_model=ResumeExtraction,
)
def extract_resume_endpoint(request: ResumeRequest):

    try:
        result = extract_resume(request.text)
        return result

    except ValueError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error),
        )
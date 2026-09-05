from fastapi import FastAPI

from src.schemas.resume import ResumeRequest, ResumeExtraction


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
def extract_resume(request: ResumeRequest):

    # Temporary stub response
    return ResumeExtraction(
        primary_role="backend_developer",
        experience_level="mid",
        years_experience=3,
        skills=[
            "Python",
            "FastAPI",
            "Docker",
        ],
        confidence=0.9,
        needs_review=False,
    )
from typing import Literal

from pydantic import BaseModel, Field


class ResumeRequest(BaseModel):
    text: str = Field(
        min_length=50,
        max_length=10000,
        description="Resume or job profile text to extract information from",
    )


class ResumeExtraction(BaseModel):
    primary_role: Literal[
        "backend_developer",
        "frontend_developer",
        "fullstack_developer",
        "data_engineer",
        "data_scientist",
        "machine_learning_engineer",
        "devops_engineer",
        "software_engineer",
        "other",
    ]

    experience_level: Literal[
        "entry",
        "junior",
        "mid",
        "senior",
        "lead",
        "unknown",
    ]

    years_experience: float | None = Field(
        default=None,
        ge=0,
        le=50,
    )

    skills: list[str] = Field(
        max_length=20,
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
    )

    needs_review: bool

class ExtractionMetadata(BaseModel):
    latency_seconds: float
    model: str


class ExtractionResponse(BaseModel):
    data: ResumeExtraction
    metadata: ExtractionMetadata
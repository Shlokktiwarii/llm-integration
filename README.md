# StructuraAI

LLM-powered structured data extraction and validation API.

StructuraAI takes unstructured text, uses an LLM to extract structured information, validates the output, and automatically attempts to repair invalid responses.

## Features

- FastAPI REST API
- Local LLM inference with Ollama
- Structured JSON extraction
- Pydantic validation
- Automatic LLM output repair
- Failed-response quarantine
- Latency measurement
- Evaluation dataset and automated evaluation runner
- Accuracy and latency metrics
- Saved evaluation results

## Architecture

Input Text
    ↓
FastAPI
    ↓
LLM (Ollama)
    ↓
JSON Parsing
    ↓
Pydantic Validation
    ↓
Valid?
    ├── Yes → Result
    │
    └── No → LLM Repair
                  ↓
             Validate Again
                  ↓
             ├── Valid → Result
             └── Failed → Quarantine

## Tech Stack

- Python
- FastAPI
- Pydantic
- Ollama
- Gemma 3
- OpenAI Python SDK
- python-dotenv

## Project Structure

llm-integration/
│
├── src/
│   ├── llm/
│   ├── prompts/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
├── evals/
│   ├── dataset.json
│   ├── runner.py
│   └── results/
│
├── .env
└── README.md

## Setup

### 1. Clone the repository

git clone <your-repository-url>
cd llm-integration

### 2. Create a virtual environment

python -m venv .venv

Activate it on Windows:

.\.venv\Scripts\Activate.ps1

### 3. Install dependencies

pip install -r requirements.txt

### 4. Install and run Ollama

Make sure Ollama is installed and the required model is available:

ollama pull gemma3:1b

### 5. Configure environment variables

Create a .env file:

LLM_BASE_URL=http://127.0.0.1:11434/v1/
LLM_API_KEY=ollama
LLM_MODEL=gemma3:1b
LLM_ENABLED=true
LLM_TIMEOUT=60

## Run the API

python -m uvicorn src.main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs

Use the /extract endpoint to submit text and receive structured output.

## Run Evaluations

python -m evals.runner

The evaluation runner tests predefined examples and reports:

- Role accuracy
- Experience-level accuracy
- Years-of-experience accuracy
- Overall field accuracy
- Average latency

Evaluation results are saved in:

evals/results/

## Example

Input:

Backend developer with 3 years of experience working with Python, FastAPI, PostgreSQL and Docker.

Output:

{
  "primary_role": "backend_developer",
  "experience_level": "mid",
  "years_experience": 3,
  "skills": [
    "Python",
    "FastAPI",
    "PostgreSQL",
    "Docker"
  ]
}

## Purpose

This project explores practical LLM engineering concepts including structured extraction, schema validation, automatic repair, failure handling, evaluation, and latency measurement.

## Status

Completed prototype.

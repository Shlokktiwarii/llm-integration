from src.llm.client import call_llm
from src.prompts.loader import load_resume_prompt


resume_text = """
Python backend developer with 3 years of experience.
Experienced in FastAPI, PostgreSQL, Docker, Redis and AWS.
"""


prompt = load_resume_prompt(resume_text)

response = call_llm(prompt)

print(response)
from fastapi import APIRouter, HTTPException
from app.services.llama import generate_questions
from app.models.request import QuestionRequest

router = APIRouter()

@router.post("/generate-questions/")
async def generate_interview_questions(request: QuestionRequest):
    """
    API endpoint to generate interview questions based on job description and candidate profile.
    """
    try:
        questions = generate_questions(
            job_description=request.job_description,
            candidate_profile=request.candidate_profile,
        )
        return {"questions": questions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



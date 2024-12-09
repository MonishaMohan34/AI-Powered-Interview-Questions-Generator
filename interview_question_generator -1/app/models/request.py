
from pydantic import BaseModel

class QuestionRequest(BaseModel):
    job_description: str
    candidate_profile: str

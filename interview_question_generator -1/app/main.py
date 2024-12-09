

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.routes import questions


app = FastAPI()


app.include_router(questions.router)


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate-questions/", response_class=HTMLResponse)
async def generate_interview_questions(request: Request, job_description: str = Form(...), candidate_profile: str = Form(...)):
    
    questions = questions.generate_questions(job_description=job_description, candidate_profile=candidate_profile)
    return templates.TemplateResponse("index.html", {"request": request, "job_description": job_description, "candidate_profile": candidate_profile, "questions": questions})
    
    
  

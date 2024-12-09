
import os
from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_NAME = "HuggingFaceTB/SmolLM-1.7B-Instruct"


HF_API_TOKEN = os.getenv("HF_API_TOKEN", "**********************")


tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HF_API_TOKEN)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, token=HF_API_TOKEN)

def generate_questions(job_description: str, candidate_profile: str) -> list:
    """
    Generate interview questions based on the job description and candidate profile.
    """
    
    prompt = f"""
    Based on the job description:
    {job_description}

    And the candidate profile:
    {candidate_profile}

    Generate technical interview questions for this candidate.
    """

    
    inputs = tokenizer(prompt, return_tensors="pt")

    
    outputs = model.generate(**inputs, max_length=40, do_sample=True)

    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.split("\n")

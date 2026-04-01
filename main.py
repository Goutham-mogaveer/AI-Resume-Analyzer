from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import PyPDF2

app = FastAPI()

def analyze_resume(text):
    score = 50
    strengths = []
    improvements = []

    # Skill checks
    if "python" in text.lower():
        strengths.append("Python skill detected")
        score += 15
    else:
        improvements.append("Add Python skill if applicable")

    if "project" in text.lower():
        strengths.append("Projects section found")
        score += 15
    else:
        improvements.append("Add a Projects section")

    if "internship" in text.lower() or "experience" in text.lower():
        strengths.append("Experience section found")
        score += 10
    else:
        improvements.append("Add internship or work experience")

    if len(text) > 500:
        strengths.append("Resume length looks good")
        score += 10
    else:
        improvements.append("Resume content is too short")

    if score > 100:
        score = 100

    return {
        "ats_score": score,
        "strengths": strengths,
        "improvements": improvements
    }

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    pdf_reader = PyPDF2.PdfReader(file.file)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    result = analyze_resume(text)

    return {
        "filename": file.filename,
        "analysis": result
    }
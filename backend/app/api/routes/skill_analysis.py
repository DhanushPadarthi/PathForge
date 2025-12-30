from fastapi import APIRouter, UploadFile, File
from app.services.resume_parser import extract_text
from app.services.section_parser import parse_sections
from app.services.skill_analyzer import extract_skills, gap_analysis

router = APIRouter()

@router.post("/analyze")
def analyze_resume(file: UploadFile = File(...)):
    text = extract_text(file.file, file.filename)
    sections = parse_sections(text)
    skills = extract_skills(text)

    return {
        "extracted_skills": skills,
        "experience_summary": sections["experience"][:500]
    }

@router.post("/gap-analysis")
def skill_gap(
    file: UploadFile = File(...),
    required_skills: list[str] = []
):
    text = extract_text(file.file, file.filename)
    skills = extract_skills(text)

    return gap_analysis(skills, required_skills)

@router.post("/questionnaire")
def questionnaire_answers(answers: dict):
    inferred_skills = []

    for key, value in answers.items():
        if value is True:
            inferred_skills.append(key.lower())

    return {
        "inferred_skills": inferred_skills,
        "message": "Skills inferred from questionnaire"
    }

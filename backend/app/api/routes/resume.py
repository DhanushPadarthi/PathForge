from fastapi import APIRouter, UploadFile, File
from app.services.resume_parser import extract_text
from app.services.section_parser import parse_sections

router = APIRouter()

@router.post("/upload")
def upload_resume(file: UploadFile = File(...)):
    text = extract_text(file.file, file.filename)
    sections = parse_sections(text)

    return {
        "message": "Resume uploaded & parsed successfully",
        "sections_detected": list(sections.keys()),
        "skills_section_preview": sections["skills"][:300]
    }

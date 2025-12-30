from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.validators import validate_resume
from app.services.resume_parser import extract_pdf, extract_docx
from app.core.database import resume_collection

resume_router = APIRouter()

@resume_router.post("/upload")
def upload_resume(file: UploadFile = File(...)):
    validate_resume(file)

    try:
        if file.filename.endswith(".pdf"):
            text = extract_pdf(file.file)
        else:
            text = extract_docx(file.file)
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to parse resume")

    resume_collection.insert_one({
        "filename": file.filename,
        "content": text
    })

    return {
        "message": "Resume uploaded successfully",
        "text_length": len(text)
    }

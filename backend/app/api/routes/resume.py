from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Dummy resume upload endpoint (can be expanded later)
    """
    if not file.filename.endswith((".pdf", ".docx")):
        raise HTTPException(
            status_code=400,
            detail="Only PDF or DOCX files are allowed",
        )

    return {
        "filename": file.filename,
        "message": "Resume uploaded successfully"
    }

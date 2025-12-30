from fastapi import APIRouter, Body
from typing import List

router = APIRouter()


@router.post("/analyze")
async def analyze_skills(payload: dict = Body(...)):
    """
    Temporary skill analysis endpoint.
    This is a placeholder to keep the API bootable.
    """
    skills = payload.get("skills", [])

    if not isinstance(skills, list):
        return {"error": "skills must be a list"}

    return {
        "input_skills": skills,
        "message": "Skill analysis completed (stub)",
        "matched_skills": skills,
        "missing_skills": []
    }

from fastapi import APIRouter, Body
from typing import List

router = APIRouter()


@router.post("/generate")
async def generate_roadmap(payload: dict = Body(...)):
    """
    Temporary roadmap generation endpoint.
    This is a placeholder to keep the API bootable.
    """
    role = payload.get("career_role")
    skills = payload.get("skills", [])

    if not role:
        return {"error": "career_role is required"}

    return {
        "career_role": role,
        "skills": skills,
        "roadmap": [
            {
                "module": "Foundation",
                "topics": skills[:2]
            },
            {
                "module": "Intermediate",
                "topics": skills[2:]
            }
        ],
        "message": "Roadmap generated (stub)"
    }

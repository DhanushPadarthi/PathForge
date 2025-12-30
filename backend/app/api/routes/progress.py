from fastapi import APIRouter, Body

router = APIRouter()


@router.post("/update")
async def update_progress(payload: dict = Body(...)):
    """
    Minimal progress endpoint to keep API bootable
    """
    return {
        "status": "ok",
        "message": "Progress endpoint working",
        "input": payload
    }

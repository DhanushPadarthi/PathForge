from fastapi import APIRouter, Depends, HTTPException, status
from app.core.dependencies import get_current_active_user
from app.config.mongodb import db

# ✅ router MUST be defined first
router = APIRouter()


@router.get("/users")
async def list_users(
    current_user: dict = Depends(get_current_active_user),
):
    users = []
    cursor = db.db.users.find({})
    async for user in cursor:
        user["_id"] = str(user["_id"])
        users.append(user)
    return users


@router.delete("/users/{user_id}")
async def delete_user(
    user_id: str,
    current_user: dict = Depends(get_current_active_user),
):
    result = await db.db.users.delete_one({"_id": user_id})
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return {"message": "User deleted successfully"}

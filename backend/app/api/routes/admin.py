# API routes for admin operations
# To be implemented

@router.delete("/users/{user_id}")
async def delete_user(user_id: str, admin: dict = Depends(get_admin_user)):
    """Delete user (Admin only)"""
    if user_id == admin["_id"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot delete your own admin account"
        )
    
    users_collection = db.get_collection("users")
    result = await users_collection.delete_one({"_id": user_id})
    
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return {"message": "User deleted successfully"}

@router.put("/users/{user_id}/toggle-active")
async def toggle_user_active(user_id: str, admin: dict = Depends(get_admin_user)):
    """Activate/Deactivate user (Admin only)"""
    users_collection = db.get_collection("users")
    user = await users_collection.find_one({"_id": user_id})
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    new_status = not user.get("is_active", True)
    await users_collection.update_one(
        {"_id": user_id},
        {"$set": {"is_active": new_status}}
    )
    
    return {"message": f"User {'activated' if new_status else 'deactivated'} successfully"}

# ===== CAREER ROLE MANAGEMENT =====

@router.post("/career-roles")
async def create_career_role(
    role: CareerRoleCreate,
    admin: dict = Depends(get_admin_user)
):
    """Create new career role (Admin only)"""
    career_roles_collection = db.get_collection("career_roles")
    
    # Check if already exists
    existing = await career_roles_collection.find_one({"_id": role.id})
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Career role with this ID already exists"
        )
    
    new_role = {
        "_id": role.id,
        **role.dict(exclude={"id"}),
        "created_at": datetime.utcnow()
    }
    
    await career_roles_collection.insert_one(new_role)
    return {"message": "Career role created successfully", "role_id": role.id}

@router.delete("/career-roles/{role_id}")
async def delete_career_role(role_id: str, admin: dict = Depends(get_admin_user)):
    """Delete career role (Admin only)"""
    career_roles_collection = db.get_collection("career_roles")
    result = await career_roles_collection.delete_one({"_id": role_id})
    
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Career role not found"
        )
    
    return {"message": "Career role deleted successfully"}

# ===== STATISTICS =====

@router.get("/statistics")
async def get_platform_statistics(admin: dict = Depends(get_admin_user)):
    """Get platform statistics (Admin only)"""
    users_collection = db.get_collection("users")
    roadmaps_collection = db.get_collection("roadmaps")
    resources_collection = db.get_collection("resources")
    career_roles_collection = db.get_collection("career_roles")
    
    total_users = await users_collection.count_documents({})
    active_users = await users_collection.count_documents({"is_active": True})
    total_roadmaps = await roadmaps_collection.count_documents({})
    completed_roadmaps = await roadmaps_collection.count_documents({"status": "completed"})
    total_resources = await resources_collection.count_documents({})
    total_career_roles = await career_roles_collection.count_documents({})
    
    return {
        "total_users": total_users,
        "active_users": active_users,
        "inactive_users": total_users - active_users,
        "total_roadmaps": total_roadmaps,
        "active_roadmaps": total_roadmaps - completed_roadmaps,
        "completed_roadmaps": completed_roadmaps,
        "completion_rate": round((completed_roadmaps / total_roadmaps * 100), 2) if total_roadmaps > 0 else 0,
        "total_resources": total_resources,
        "total_career_roles": total_career_roles
    }
# DELETE /api/admin/resources/{resource_id} - Delete resource

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


# =============================
# Base Schema
# =============================

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None


# =============================
# Auth Request Schemas
# =============================

class UserSignupRequest(UserBase):
    password: str


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserUpdateRequest(BaseModel):
    """
    Used for profile updates
    """
    full_name: Optional[str] = None
    password: Optional[str] = None


class PasswordChangeRequest(BaseModel):
    """
    Used for changing password
    """
    current_password: str
    new_password: str


# Backward compatibility (if used elsewhere)
class UserCreate(UserSignupRequest):
    pass


# =============================
# Auth Response Schemas
# =============================

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# =============================
# User Response Schema
# =============================

class UserResponse(BaseModel):
    id: str = Field(..., description="User ID")
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True
    created_at: Optional[datetime] = None

    @classmethod
    def from_mongo(cls, user: dict):
        """
        Convert MongoDB document to API response safely
        """
        return cls(
            id=str(user.get("_id")),
            email=user.get("email"),
            full_name=user.get("full_name"),
            is_active=user.get("is_active", True),
            created_at=user.get("created_at"),
        )

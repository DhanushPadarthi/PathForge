from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime


class UserSignupRequest(BaseModel):
    """Schema for user signup request"""
    email: EmailStr
    password: str = Field(..., min_length=8, description="Password must be at least 8 characters")
    name: str = Field(..., min_length=2, max_length=100)


class UserLoginRequest(BaseModel):
    """Schema for user login request"""
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """Schema for user response (no sensitive data)"""
    _id: str = Field(..., alias="_id")
    email: str
    name: str
    role: str = "user"
    is_active: bool = True
    has_resume: bool = False
    resume_url: Optional[str] = None
    resume_filename: Optional[str] = None
    extracted_skills: List[str] = []
    career_role_id: Optional[str] = None
    learning_time: Optional[str] = None
    deadline: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "123e4567-e89b-12d3-a456-426614174000",
                "email": "user@example.com",
                "name": "John Doe",
                "role": "user",
                "is_active": True,
                "has_resume": False,
                "extracted_skills": ["Python", "JavaScript"],
                "created_at": "2024-01-01T00:00:00",
                "updated_at": "2024-01-01T00:00:00"
            }
        }


class TokenResponse(BaseModel):
    """Schema for authentication token response"""
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


class UserUpdateRequest(BaseModel):
    """Schema for updating user profile"""
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    learning_time: Optional[str] = None
    deadline: Optional[datetime] = None


class PasswordChangeRequest(BaseModel):
    """Schema for changing password"""
    current_password: str
    new_password: str = Field(..., min_length=8, description="New password must be at least 8 characters")

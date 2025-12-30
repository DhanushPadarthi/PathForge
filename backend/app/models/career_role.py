# Career role model
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class CareerRole(BaseModel):
    """Model representing a career role with required skills and metadata"""
    id: Optional[str] = Field(None, alias="_id")
    title: str
    description: str
    required_skills: List[str]
    recommended_skills: List[str] = []
    average_learning_hours: int
    difficulty_level: str  # beginner, intermediate, advanced
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "title": "Full Stack Developer",
                "description": "Develops both frontend and backend applications",
                "required_skills": ["HTML", "CSS", "JavaScript", "React", "Node.js", "MongoDB"],
                "recommended_skills": ["TypeScript", "Docker", "AWS"],
                "average_learning_hours": 200,
                "difficulty_level": "intermediate"
            }
        }

class CareerRoleCreate(BaseModel):
    """Schema for creating a new career role"""
    title: str
    description: str
    required_skills: List[str]
    recommended_skills: List[str] = []
    average_learning_hours: int
    difficulty_level: str

class CareerRoleUpdate(BaseModel):
    """Schema for updating an existing career role"""
    title: Optional[str] = None
    description: Optional[str] = None
    required_skills: Optional[List[str]] = None
    recommended_skills: Optional[List[str]] = None
    average_learning_hours: Optional[int] = None
    difficulty_level: Optional[str] = None

class CareerRoleResponse(BaseModel):
    """Response schema for career role queries"""
    id: str = Field(alias="_id")
    title: str
    description: str
    required_skills: List[str]
    recommended_skills: List[str]
    average_learning_hours: int
    difficulty_level: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        populate_by_name = True

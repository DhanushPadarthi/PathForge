# Roadmap schemas
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum

# Enums
class ResourceStatus(str, Enum):
    """Status of a learning resource"""
    LOCKED = "locked"
    UNLOCKED = "unlocked"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    SKIPPED = "skipped"

# Request/Response Schemas
class SkillGapSchema(BaseModel):
    """Schema for skill gap information"""
    skill: str
    current_level: str
    required_level: str
    gap_severity: str
    learning_priority: str

class LearningResourceSchema(BaseModel):
    """Schema for learning resource"""
    id: str
    title: str
    url: str
    description: Optional[str] = None
    estimated_hours: float
    resource_type: str  # video, article, course, practice
    status: ResourceStatus = ResourceStatus.LOCKED
    completed_at: Optional[datetime] = None
    skipped_at: Optional[datetime] = None
    opened_at: Optional[datetime] = None
    time_spent_seconds: int = 0
    order: int

class ModuleSchema(BaseModel):
    """Schema for learning module"""
    id: str
    title: str
    description: str
    skills_covered: List[str]
    resources: List[LearningResourceSchema]
    estimated_total_hours: float
    week_number: int
    order: int
    is_completed: bool = False
    completion_percentage: float = 0.0

class RoadmapCreate(BaseModel):
    """Schema for creating a new roadmap"""
    target_role: str
    skill_gaps: List[SkillGapSchema]
    modules: List[ModuleSchema]
    total_estimated_hours: float
    deadline: datetime

class RoadmapUpdate(BaseModel):
    """Schema for updating roadmap progress"""
    progress_percentage: Optional[float] = None
    current_module_index: Optional[int] = None
    modules: Optional[List[ModuleSchema]] = None

class ResourceProgressUpdate(BaseModel):
    """Schema for updating resource progress"""
    status: ResourceStatus
    time_spent_seconds: Optional[int] = None

class ModuleCompleteRequest(BaseModel):
    """Schema for completing a module"""
    module_id: str
    completion_notes: Optional[str] = None

class RoadmapResponse(BaseModel):
    """Response schema for roadmap queries"""
    id: str = Field(alias="_id")
    user_id: str
    target_role: str
    skill_gaps: List[SkillGapSchema]
    modules: List[ModuleSchema]
    total_estimated_hours: float
    deadline: datetime
    progress_percentage: float
    current_module_index: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        populate_by_name = True

class RoadmapSummary(BaseModel):
    """Summary schema for roadmap listing"""
    id: str = Field(alias="_id")
    target_role: str
    total_estimated_hours: float
    progress_percentage: float
    deadline: datetime
    created_at: datetime
    modules_count: int
    completed_modules: int
    
    class Config:
        populate_by_name = True

class GenerateRoadmapRequest(BaseModel):
    """Schema for AI roadmap generation request"""
    target_role_id: str
    available_hours_per_week: int
    deadline_weeks: int
    preferred_learning_style: Optional[str] = "balanced"  # visual, reading, practice, balanced
    focus_areas: Optional[List[str]] = []

class ModuleSummary(BaseModel):
    """Summary of completed module"""
    module_id: str
    module_title: str
    skills_covered: List[str]
    time_spent_hours: float
    resources_completed: int
    resources_skipped: int
    completion_date: datetime
    next_module_title: Optional[str] = None

class RoadmapProgressStats(BaseModel):
    """Overall roadmap progress statistics"""
    total_modules: int
    completed_modules: int
    total_resources: int
    completed_resources: int
    skipped_resources: int
    total_hours_estimated: float
    hours_completed: float
    hours_remaining: float
    completion_percentage: float
    average_hours_per_week: float
    estimated_completion_date: datetime
    on_track: bool

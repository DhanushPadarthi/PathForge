from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class Resource(BaseModel):
    id: Optional[str] = None
    skill: str
    title: str
    link: HttpUrl
    estimated_time_minutes: int
    created_at: datetime = datetime.utcnow()

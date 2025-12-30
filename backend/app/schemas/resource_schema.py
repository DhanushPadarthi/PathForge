from pydantic import BaseModel
from typing import List

class ResourceRequest(BaseModel):
    skills: List[str]

from fastapi import FastAPI
from app.api.routes.resume import router as resume_router
from app.api.routes.skill_analysis import router as skill_router

app = FastAPI(title="PathForge Resume Analyzer")

@app.get("/")
def root():
    return {"message": "PathForge backend is running"}

app.include_router(resume_router, prefix="/api/resume", tags=["Resume"])
app.include_router(skill_router, prefix="/api/skills", tags=["Skill Analysis"])

from fastapi import FastAPI
from app.api.routes.resume import router as resume_router

app = FastAPI(title="PathForge API")

@app.get("/")
def root():
    return {"message": "PathForge backend is running"}

app.include_router(
    resume_router,
    prefix="/api/resume",
    tags=["Resume"]
)

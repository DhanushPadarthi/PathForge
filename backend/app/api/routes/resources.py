from fastapi import APIRouter
from app.schemas.resource_schema import ResourceRequest
from app.services.resource_recommender import ResourceRecommenderService

router = APIRouter()

@router.post("/")
async def recommend_resources(payload: ResourceRequest):
    return ResourceRecommenderService.recommend_resources(
        payload.model_dump()
    )

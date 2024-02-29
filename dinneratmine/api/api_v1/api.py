from fastapi import APIRouter

from dinneratmine.api.api_v1.endpoints import recipe


api_router = APIRouter()
api_router.include_router(recipe.router, prefix="/recipes", tags=["recipes"])
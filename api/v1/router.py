from fastapi import APIRouter

from api.v1.endpoints.image_analysis import router as image_analysis_router
from api.v1.endpoints.environment_diagnosis import router as environment_diagnosis_router
from api.v1.endpoints import plant

api_router = APIRouter()

api_router.include_router(image_analysis_router, prefix="/analysis", tags=["Image Analysis"])
api_router.include_router(environment_diagnosis_router, prefix="/diagnosis", tags=["Environment Diagnosis"])
api_router.include_router(plant.router, prefix="/plants", tags=["plants"])

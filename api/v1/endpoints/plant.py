from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from crud.plant import get_plants, get_plants_by_env_type, get_plant
from db.session import get_db
from schemas.plant import PlantRecommendResponse, PlantResponse

router = APIRouter()

DbDep = Annotated[AsyncSession, Depends(get_db)]


@router.get("", response_model=list[PlantResponse])
async def list_plants(db: DbDep):
    plants = await get_plants(db)
    return plants


@router.get("/recommend", response_model=PlantRecommendResponse)
async def recommend_plants(env_type_id: str, db: DbDep):
    env_type, optimal, possible = await get_plants_by_env_type(db, env_type_id)

    if env_type is None:
        raise HTTPException(status_code=404, detail=f"환경 유형 '{env_type_id}'을 찾을 수 없습니다.")

    return PlantRecommendResponse(
        env_type=env_type,
        optimal=optimal,
        possible=possible,
    )


@router.get("/{plant_id}", response_model=PlantResponse)
async def get_plant_detail(plant_id: str, db: DbDep):
    plant = await get_plant(db, plant_id)
    if plant is None:
        raise HTTPException(status_code=404, detail=f"식물 ID '{plant_id}'을 찾을 수 없습니다.")
    return plant


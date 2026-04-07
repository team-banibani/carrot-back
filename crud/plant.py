from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models.environment_type import EnvironmentType
from models.enums import FitEnum
from models.plant import Plant
from models.plant_environment import PlantEnvironment


async def get_plants(db: AsyncSession) -> list[Plant]:
    result = await db.execute(select(Plant))
    return list(result.scalars().all())


async def get_plants_by_env_type(
    db: AsyncSession, env_type_id: str
) -> tuple[EnvironmentType | None, list[Plant], list[Plant]]:
    env_result = await db.execute(
        select(EnvironmentType).where(EnvironmentType.id == env_type_id)
    )
    env_type = env_result.scalar_one_or_none()

    if env_type is None:
        return None, [], []

    mapping_result = await db.execute(
        select(PlantEnvironment)
        .options(selectinload(PlantEnvironment.plant))
        .where(PlantEnvironment.env_type_id == env_type_id)
    )
    mappings = list(mapping_result.scalars().all())

    optimal = [m.plant for m in mappings if m.fit == FitEnum.OPTIMAL]
    possible = [m.plant for m in mappings if m.fit == FitEnum.POSSIBLE]

    return env_type, optimal, possible

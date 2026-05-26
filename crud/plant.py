from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models.categories import Categories
from models.environment_type import EnvironmentType
from models.enums import CategoryLevelEnum
from models.plant import Plant


async def get_plants(db: AsyncSession, sort_by_views: bool = False) -> list[Plant]:
    stmt = select(Plant)
    if sort_by_views:
        stmt = stmt.order_by(Plant.view_count.desc())
    result = await db.execute(stmt)
    return list(result.scalars().all())


async def get_plant(db: AsyncSession, plant_id: str) -> Plant | None:
    await db.execute(
        update(Plant)
        .where(Plant.id == plant_id)
        .values(view_count=Plant.view_count + 1)
    )
    await db.commit()

    result = await db.execute(select(Plant).where(Plant.id == plant_id))
    return result.scalar_one_or_none()


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
        select(Categories)
        .options(selectinload(Categories.plant))
        .where(Categories.env_type_id == env_type_id)
    )
    mappings = list(mapping_result.scalars().all())

    optimal = [m.plant for m in mappings if m.level == CategoryLevelEnum.OPTIMAL]
    possible = [m.plant for m in mappings if m.level == CategoryLevelEnum.POSSIBLE]

    return env_type, optimal, possible

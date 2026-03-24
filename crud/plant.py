from sqlalchemy.ext.asyncio import AsyncSession


async def get_plant(db: AsyncSession, plant_id: str):
    pass


async def get_plants(db: AsyncSession, skip: int = 0, limit: int = 100):
    pass


async def create_plant(db: AsyncSession, data: dict):
    pass


async def update_plant(db: AsyncSession, plant_id: str, data: dict):
    pass


async def delete_plant(db: AsyncSession, plant_id: str):
    pass

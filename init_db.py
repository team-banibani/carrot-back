import asyncio
from db.session import engine
from db.base import Base

# Import all models to ensure they are registered on Base.metadata
from models.environment_type import EnvironmentType
from models.plant import Plant
from models.recommended_location import RecommendedLocation
from models.mapping import Mapping
from models.categories import Categories

async def init_models():
    async with engine.begin() as conn:
        # Create all tables
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables created successfully!")

if __name__ == "__main__":
    asyncio.run(init_models())

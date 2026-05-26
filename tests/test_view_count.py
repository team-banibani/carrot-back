"""조회수 증가 및 정렬 기능 테스트 (SQLite 인메모리 DB 사용)"""
import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from db.base import Base
from models.enums import (
    AirPurificationEnum,
    ManagementDifficultyEnum,
    PetStabilityEnum,
    SizeEnum,
    SunlightRequirementsEnum,
)
from models.plant import Plant
from crud.plant import get_plant, get_plants

DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest_asyncio.fixture
async def db():
    engine = create_async_engine(DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


def make_plant(plant_id: str, name_ko: str, view_count: int = 0) -> Plant:
    return Plant(
        id=plant_id,
        name_ko=name_ko,
        name_en=name_ko,
        management_difficulty=ManagementDifficultyEnum.EASY,
        watering="2주 1회",
        appropriate_temperature="18~25°C",
        appropriate_humidity="40~60%",
        sunlight_requirements=SunlightRequirementsEnum.LOW,
        size=SizeEnum.SMALL,
        air_purification_effect=AirPurificationEnum.NORMAL,
        pet_stability=PetStabilityEnum.SAFE,
        view_count=view_count,
    )


@pytest.mark.asyncio
async def test_view_count_increments_on_detail(db: AsyncSession):
    """상세 조회 시 조회수가 1씩 증가하는지 확인"""
    plant = make_plant("PLT-001", "스킨답서스", view_count=0)
    db.add(plant)
    await db.commit()

    result = await get_plant(db, "PLT-001")
    assert result is not None
    assert result.view_count == 1, f"1회 조회 후 view_count=1이어야 함 (실제: {result.view_count})"

    await get_plant(db, "PLT-001")
    await get_plant(db, "PLT-001")
    result = await get_plant(db, "PLT-001")
    assert result.view_count == 4, f"4회 조회 후 view_count=4이어야 함 (실제: {result.view_count})"
    print(f"\n✅ 조회수 증가: 4회 조회 → view_count={result.view_count}")


@pytest.mark.asyncio
async def test_get_plant_not_found(db: AsyncSession):
    """존재하지 않는 식물 ID 조회 시 None 반환"""
    result = await get_plant(db, "PLT-999")
    assert result is None
    print("\n✅ 없는 plant_id 조회 → None 반환")


@pytest.mark.asyncio
async def test_list_sorted_by_views(db: AsyncSession):
    """조회수 내림차순 정렬 확인"""
    plants = [
        make_plant("PLT-001", "스킨답서스", view_count=5),
        make_plant("PLT-002", "산세베리아", view_count=20),
        make_plant("PLT-003", "몬스테라", view_count=1),
    ]
    for p in plants:
        db.add(p)
    await db.commit()

    sorted_plants = await get_plants(db, sort_by_views=True)
    counts = [p.view_count for p in sorted_plants]
    assert counts == sorted(counts, reverse=True), f"조회수 내림차순이어야 함: {counts}"
    print(f"\n✅ 조회수 내림차순 정렬: {[(p.name_ko, p.view_count) for p in sorted_plants]}")


@pytest.mark.asyncio
async def test_list_default_order(db: AsyncSession):
    """정렬 옵션 없을 때는 기본 순서(삽입 순)로 반환"""
    plants = [
        make_plant("PLT-001", "스킨답서스", view_count=5),
        make_plant("PLT-002", "산세베리아", view_count=20),
    ]
    for p in plants:
        db.add(p)
    await db.commit()

    result = await get_plants(db, sort_by_views=False)
    ids = [p.id for p in result]
    assert ids == ["PLT-001", "PLT-002"]
    print(f"\n✅ 기본 순서 유지: {ids}")

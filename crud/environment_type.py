from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, case, or_
from models.environment_type import EnvironmentType
from models.enums import SunlightEnum, TemperatureEnum, HumidityEnum


async def get_environment_type_by_conditions(
    session: AsyncSession,
    sunlight: SunlightEnum,
    temperature: TemperatureEnum,
    humidity: HumidityEnum
) -> EnvironmentType | None:
    """
    조건에 맞는 환경 유형 조회 (우선순위 기반 정렬)
    
    한 번의 쿼리로 모든 조건을 확인하고 우선순위로 정렬:
    - 우선순위 1: 햇빛 + 온도 + 습도 모두 일치
    - 우선순위 2: 햇빛 + 온도 일치
    - 우선순위 3: 햇빛 + 습도 일치
    - 우선순위 4: 햇빛만 일치
    - 우선순위 5: 온도 + 습도 일치
    - 우선순위 6: 온도만 일치
    - 우선순위 7: 습도만 일치
    
    Args:
        session: DB 세션
        sunlight: 햇빛 조건
        temperature: 온도 조건
        humidity: 습도 조건
        
    Returns:
        우선순위가 가장 높은 EnvironmentType 객체 또는 None
    """
    
    # 우선순위 계산 로직
    priority = case(
        # 1순위: 3개 조건 모두 일치
        (
            (EnvironmentType.sunlight == sunlight) &
            (EnvironmentType.temperature == temperature) &
            (EnvironmentType.humidity == humidity),
            1
        ),
        # 2순위: 햇빛 + 온도 일치
        (
            (EnvironmentType.sunlight == sunlight) &
            (EnvironmentType.temperature == temperature),
            2
        ),
        # 3순위: 햇빛 + 습도 일치
        (
            (EnvironmentType.sunlight == sunlight) &
            (EnvironmentType.humidity == humidity),
            3
        ),
        # 4순위: 햇빛만 일치
        (EnvironmentType.sunlight == sunlight, 4),
        # 5순위: 온도 + 습도 일치
        (
            (EnvironmentType.temperature == temperature) &
            (EnvironmentType.humidity == humidity),
            5
        ),
        # 6순위: 온도만 일치
        (EnvironmentType.temperature == temperature, 6),
        # 7순위: 습도만 일치
        (EnvironmentType.humidity == humidity, 7),
        # 매칭 안 됨
        else_=8
    )
    
    # CASE가 상세 우선순위를 계산하므로, WHERE는 "하나라도 일치"만 확인하면 충분
    stmt = (
        select(EnvironmentType)
        .where(
            or_(
                EnvironmentType.sunlight == sunlight,
                EnvironmentType.temperature == temperature,
                EnvironmentType.humidity == humidity,
            )
        )
        .order_by(priority, EnvironmentType.id)
        .limit(1)
    )
    
    result = await session.execute(stmt)
    return result.scalars().first()

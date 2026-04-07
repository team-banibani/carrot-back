from sqlalchemy.ext.asyncio import AsyncSession

from crud import environment_type as env_type_crud
from models.enums import SunlightEnum, TemperatureEnum, HumidityEnum


class EnvironmentDiagnosisService:
    """환경 진단 비즈니스 로직"""

    async def diagnose_environment_id(
        self,
        session: AsyncSession,
        sunlight: SunlightEnum,
        temperature: TemperatureEnum,
        humidity: HumidityEnum,
    ) -> str:
        """변환된 Enum 조건으로 환경 유형 ID를 조회"""
        environment_type = await env_type_crud.get_environment_type_by_conditions(
            session,
            sunlight,
            temperature,
            humidity,
        )

        if not environment_type:
            raise ValueError("매칭되는 환경 타입을 찾을 수 없습니다")

        return environment_type.id

import enum

from pydantic import BaseModel, Field

from models.enums import SunlightEnum


class SunlightInputEnum(str, enum.Enum):
    VERY_HIGH = "VERY_HIGH"
    HIGH = "HIGH"
    NORMAL_TO_HIGH = "NORMAL_TO_HIGH"
    NORMAL = "NORMAL"
    LOW_TO_NORMAL = "LOW_TO_NORMAL"
    LOW = "LOW"
    VERY_LOW = "VERY_LOW"


SUNLIGHT_INPUT_MAP: dict[SunlightInputEnum, SunlightEnum] = {
    SunlightInputEnum.VERY_HIGH: SunlightEnum.VERY_HIGH,
    SunlightInputEnum.HIGH: SunlightEnum.HIGH,
    SunlightInputEnum.NORMAL_TO_HIGH: SunlightEnum.MEDIUM,
    SunlightInputEnum.NORMAL: SunlightEnum.NORMAL,
    SunlightInputEnum.LOW_TO_NORMAL: SunlightEnum.LOW_MEDIUM,
    SunlightInputEnum.LOW: SunlightEnum.LOW,
    SunlightInputEnum.VERY_LOW: SunlightEnum.VERY_LOW,
}


class EnvironmentDiagnosisRequest(BaseModel):
    sunlight: SunlightInputEnum = Field(..., description="햇빛 조건 (예: HIGH)")
    temperature: float = Field(..., description="온도 (숫자, 예: 24.6)")
    humidity: str = Field(..., description="습도 (예: 60%)")


class EnvironmentDiagnosisResponse(BaseModel):
    environment_id: str = Field(..., description="환경 유형 ID (예: ENV-01)")

from pydantic import BaseModel, Field
from models.enums import SunlightEnum


class EnvironmentDiagnosisRequest(BaseModel):
    """환경 진단 API 요청"""
    sunlight: SunlightEnum = Field(..., description="햇빛 조건 (예: HIGH)")
    temperature: float = Field(..., description="온도 (숫자, 예: 24.6)")
    humidity: str = Field(..., description="습도 (예: 60%)")


class EnvironmentDiagnosisResponse(BaseModel):
    """환경 진단 API 응답"""
    environment_id: str = Field(..., description="환경 유형 ID (예: ENV-01)")



from pydantic import BaseModel
from models.enums import StyleEnum, SunlightEnum, SizeEnum, LocationEnum


class ImageAnalysisResponse(BaseModel):
    """사진 분석 API 응답"""
    style: StyleEnum
    sunlight: SunlightEnum
    size: SizeEnum
    place: LocationEnum


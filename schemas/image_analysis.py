from pydantic import BaseModel, field_serializer
from models.enums import StyleEnum, SunlightEnum, SizeEnum, LocationEnum


class ImageAnalysisResponse(BaseModel):
    """사진 분석 API 응답"""
    style: StyleEnum
    sunlight: SunlightEnum
    size: SizeEnum
    place: LocationEnum

    @field_serializer("style", "sunlight", "size", "place")
    def serialize_enum_label(self, val) -> str:
        return val.label

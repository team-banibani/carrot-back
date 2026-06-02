from pydantic import BaseModel, field_serializer

from models.enums import (
    AirPurificationEnum,
    ManagementDifficultyEnum,
    PetStabilityEnum,
    SizeEnum,
    SunlightRequirementsEnum,
)


class PlantResponse(BaseModel):
    model_config = {"from_attributes": True}

    id: str
    name_ko: str
    name_en: str
    management_difficulty: ManagementDifficultyEnum
    watering: str
    appropriate_temperature: str
    appropriate_humidity: str
    sunlight_requirements: SunlightRequirementsEnum
    size: SizeEnum
    air_purification_effect: AirPurificationEnum
    pet_stability: PetStabilityEnum
    explanation: str | None = None
    view_count: int = 0
    image_path: str | None = None

    @field_serializer("management_difficulty", "sunlight_requirements", "size", "air_purification_effect", "pet_stability")
    def serialize_enum_label(self, val) -> str:
        return val.label


class EnvironmentTypeSimple(BaseModel):
    model_config = {"from_attributes": True}

    id: str
    name: str


class PlantRecommendResponse(BaseModel):
    env_type: EnvironmentTypeSimple
    optimal: list[PlantResponse]
    possible: list[PlantResponse]

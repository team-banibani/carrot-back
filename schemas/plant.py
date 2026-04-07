from pydantic import BaseModel

from models.enums import (
    AirPurificationEnum,
    HumidityEnum,
    ManagementDifficultyEnum,
    PetStabilityEnum,
    SizeEnum,
    SunlightEnum,
    TemperatureEnum,
    WateringEnum,
)


class PlantResponse(BaseModel):
    model_config = {"from_attributes": True}

    id: str
    name_ko: str
    name_en: str
    management_difficulty: ManagementDifficultyEnum
    watering: WateringEnum
    appropriate_temperature: TemperatureEnum
    appropriate_humidity: HumidityEnum
    sunlight_requirements: SunlightEnum
    size: SizeEnum
    air_purification_effect: AirPurificationEnum
    pet_stability: PetStabilityEnum
    explanation: str | None = None


class EnvironmentTypeSimple(BaseModel):
    model_config = {"from_attributes": True}

    id: str
    name: str


class PlantRecommendResponse(BaseModel):
    env_type: EnvironmentTypeSimple
    optimal: list[PlantResponse]
    possible: list[PlantResponse]

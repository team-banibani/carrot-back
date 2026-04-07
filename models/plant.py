from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
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


class Plant(Base):
    __tablename__ = "plant"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name_ko: Mapped[str] = mapped_column(String(100))
    name_en: Mapped[str] = mapped_column(String(100))
    environment_type_id: Mapped[str] = mapped_column(String(36), ForeignKey("environment_type.id"))
    management_difficulty: Mapped[ManagementDifficultyEnum] = mapped_column(Enum(ManagementDifficultyEnum))
    watering: Mapped[WateringEnum] = mapped_column(Enum(WateringEnum))
    appropriate_temperature: Mapped[TemperatureEnum] = mapped_column(Enum(TemperatureEnum))
    appropriate_humidity: Mapped[HumidityEnum] = mapped_column(Enum(HumidityEnum))
    sunlight_requirements: Mapped[SunlightEnum] = mapped_column(Enum(SunlightEnum))
    size: Mapped[SizeEnum] = mapped_column(Enum(SizeEnum))
    air_purification_effect: Mapped[AirPurificationEnum] = mapped_column(Enum(AirPurificationEnum))
    pet_stability: Mapped[PetStabilityEnum] = mapped_column(Enum(PetStabilityEnum))
    explanation: Mapped[str | None] = mapped_column(String(500), nullable=True)

    environment_type: Mapped["EnvironmentType"] = relationship("EnvironmentType", back_populates="plants")
    recommended_locations: Mapped[list["RecommendedLocation"]] = relationship(
        "RecommendedLocation", back_populates="plant"
    )
    plant_environments: Mapped[list["PlantEnvironment"]] = relationship(
        "PlantEnvironment", back_populates="plant"
    )

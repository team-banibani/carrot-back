from sqlalchemy import Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
from models.enums import (
    AirPurificationEnum,
    ManagementDifficultyEnum,
    PetStabilityEnum,
    SizeEnum,
    SunlightRequirementsEnum,
)


class Plant(Base):
    __tablename__ = "plant_info"

    id: Mapped[str] = mapped_column(String(10), primary_key=True)  # PLT-001 ~ PLT-032
    name_ko: Mapped[str] = mapped_column(String(50))
    name_en: Mapped[str] = mapped_column(String(50))
    management_difficulty: Mapped[ManagementDifficultyEnum] = mapped_column(Enum(ManagementDifficultyEnum))
    watering: Mapped[str] = mapped_column(String(50))               # 예: "2~3주 1회"
    appropriate_temperature: Mapped[str] = mapped_column(String(20)) # 예: "18~30°C"
    appropriate_humidity: Mapped[str] = mapped_column(String(20))    # 예: "40~60%"
    sunlight_requirements: Mapped[SunlightRequirementsEnum] = mapped_column(Enum(SunlightRequirementsEnum))
    size: Mapped[SizeEnum] = mapped_column(Enum(SizeEnum))
    air_purification_effect: Mapped[AirPurificationEnum] = mapped_column(Enum(AirPurificationEnum))
    pet_stability: Mapped[PetStabilityEnum] = mapped_column(Enum(PetStabilityEnum))
    explanation: Mapped[str | None] = mapped_column(String(500), nullable=True)
    view_count: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
    image_path: Mapped[str | None] = mapped_column(String(1024), nullable=True)

    categories: Mapped[list["Categories"]] = relationship("Categories", back_populates="plant")
    recommended_locations: Mapped[list["RecommendedLocation"]] = relationship(
        "RecommendedLocation", back_populates="plant"
    )

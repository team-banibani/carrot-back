from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
from models.enums import HumidityEnum, SunlightEnum, TemperatureEnum, VentilationEnum


class EnvironmentType(Base):
    __tablename__ = "environment_type"

    id: Mapped[str] = mapped_column(String(10), primary_key=True)  # ENV-01 ~ ENV-09
    name: Mapped[str] = mapped_column(String(50))
    sunlight: Mapped[SunlightEnum] = mapped_column(Enum(SunlightEnum, name="sunlight_condition", create_type=False))
    ventilation: Mapped[VentilationEnum] = mapped_column(Enum(VentilationEnum, name="ventilation_condition", create_type=False))
    temperature: Mapped[TemperatureEnum] = mapped_column(Enum(TemperatureEnum, name="temperature_condition", create_type=False))
    humidity: Mapped[HumidityEnum] = mapped_column(Enum(HumidityEnum, name="humidity_condition", create_type=False))
    explanation: Mapped[str | None] = mapped_column(String(500), nullable=True)

    categories: Mapped[list["Categories"]] = relationship("Categories", back_populates="environment_type")
    mappings: Mapped[list["Mapping"]] = relationship("Mapping", back_populates="environment_type")

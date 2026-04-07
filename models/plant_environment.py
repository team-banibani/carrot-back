from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
from models.enums import FitEnum


class PlantEnvironment(Base):
    __tablename__ = "categories"

    plant_id: Mapped[str] = mapped_column(String(36), ForeignKey("plant.id"), primary_key=True)
    env_type_id: Mapped[str] = mapped_column(String(36), ForeignKey("environment_type.id"), primary_key=True)
    fit: Mapped[FitEnum] = mapped_column(Enum(FitEnum))

    plant: Mapped["Plant"] = relationship("Plant", back_populates="plant_environments")
    environment_type: Mapped["EnvironmentType"] = relationship("EnvironmentType", back_populates="plant_environments")

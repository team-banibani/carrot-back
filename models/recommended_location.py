from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
from models.enums import LocationEnum


class RecommendedLocation(Base):
    __tablename__ = "recommended_location"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    plant_id: Mapped[str] = mapped_column(String(36), ForeignKey("plant.id"))
    location: Mapped[LocationEnum] = mapped_column(Enum(LocationEnum))

    plant: Mapped["Plant"] = relationship("Plant", back_populates="recommended_locations")

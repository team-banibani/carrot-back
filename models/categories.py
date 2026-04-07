from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
from models.enums import CategoryLevelEnum


class Categories(Base):
    """유형별 추천 매트릭스 - 식물과 환경 유형 간의 적합도 매핑"""
    __tablename__ = "categories"

    plant_id: Mapped[str] = mapped_column(String(10), ForeignKey("plant_info.id"), primary_key=True)
    env_type_id: Mapped[str] = mapped_column(String(10), ForeignKey("environment_type.id"), primary_key=True)
    level: Mapped[CategoryLevelEnum] = mapped_column(Enum(CategoryLevelEnum))  # O=최적, △=가능

    plant: Mapped["Plant"] = relationship("Plant", back_populates="categories")
    environment_type: Mapped["EnvironmentType"] = relationship("EnvironmentType", back_populates="categories")

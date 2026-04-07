from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
from models.enums import CategoryEnum


class Mapping(Base):
    __tablename__ = "Mapping"

    category: Mapped[CategoryEnum] = mapped_column(Enum(CategoryEnum))  # 햇빛/통풍/온도/습도
    keyword_id: Mapped[str] = mapped_column(String(10), primary_key=True)  # KW-S01 등
    display_keyword: Mapped[str] = mapped_column(String(50))
    env_condition: Mapped[str | None] = mapped_column(String(100), nullable=True)
    env_type_id: Mapped[str | None] = mapped_column(String(10), ForeignKey("environment_type.id"), nullable=True)

    environment_type: Mapped["EnvironmentType | None"] = relationship("EnvironmentType", back_populates="mappings")

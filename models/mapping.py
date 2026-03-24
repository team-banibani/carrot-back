from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base


class Mapping(Base):
    __tablename__ = "Mapping"

    category: Mapped[str] = mapped_column(String(100))
    keyword_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    display_keyword: Mapped[str] = mapped_column(String(100))
    env_condition: Mapped[str | None] = mapped_column(String(200), nullable=True)
    env_type_id: Mapped[str | None] = mapped_column(String(36), ForeignKey("environment_type.id"), nullable=True)

    environment_type: Mapped["EnvironmentType | None"] = relationship("EnvironmentType", back_populates="mappings")

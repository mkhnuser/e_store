from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Seller(Base):
    __tablename__ = "seller"
    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    name: Mapped[str]
    email: Mapped[str]

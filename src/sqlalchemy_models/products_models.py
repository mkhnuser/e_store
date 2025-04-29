from sqlalchemy import Numeric
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    name: Mapped[str]
    price: Mapped[Numeric]

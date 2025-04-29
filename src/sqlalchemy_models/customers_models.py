from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Customer(Base):
    __tablename__ = "customer"
    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    name: Mapped[str]
    age: Mapped[int]

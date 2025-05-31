import datetime as dt
from typing import Optional
from decimal import Decimal

from sqlalchemy import DateTime, String, Table, Column, ForeignKey, Numeric, MetaData
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_`%(constraint_name)s`",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )


class ProductDatabaseModel(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
    price: Mapped[Decimal] = mapped_column(Numeric())

    created_at: Mapped[dt.datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[dt.datetime] = mapped_column(
        DateTime,
        default=dt.datetime.now,
    )

    reviews: Mapped[list["ProductReviewDatabaseModel"]] = relationship(
        back_populates="product"
    )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.id}, {self.name})"

    def __repr__(self) -> str:
        return str(self)


class ProductReviewDatabaseModel(Base):
    __tablename__ = "product_reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int]
    text: Mapped[Optional[str]]

    created_at: Mapped[dt.datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[dt.datetime] = mapped_column(
        DateTime,
        default=dt.datetime.now,
    )

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped[ProductDatabaseModel] = relationship(back_populates="reviews")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.id}, {self.rating}, {self.text})"

    def __repr__(self) -> str:
        return str(self)


users_roles_table = Table(
    "users_roles",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
)


class RoleDatabaseModel(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    description: Mapped[Optional[str]]

    created_at: Mapped[dt.datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[dt.datetime] = mapped_column(
        DateTime,
        default=dt.datetime.now,
    )

    users: Mapped[list["UserDatabaseModel"]] = relationship(
        secondary="users_roles",
        back_populates="roles",
    )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.id}, {self.name})"

    def __repr__(self) -> str:
        return str(self)


class UserDatabaseModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    phone_number: Mapped[Optional[str]] = mapped_column(unique=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str] = mapped_column(String(256))
    first_name: Mapped[str]
    last_name: Mapped[Optional[str]]

    created_at: Mapped[dt.datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[dt.datetime] = mapped_column(
        DateTime,
        default=dt.datetime.now,
    )

    roles: Mapped[list[RoleDatabaseModel]] = relationship(
        secondary="users_roles",
        back_populates="users",
    )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.id}, {self.email})"

    def __repr__(self) -> str:
        return str(self)

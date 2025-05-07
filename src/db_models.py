from typing import Optional

from sqlalchemy import Table, Column, ForeignKey, Numeric, MetaData
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
    price: Mapped[float] = mapped_column(Numeric())
    reviews: Mapped[list["ProductReviewDatabaseModel"]] = relationship(
        back_populates="product"
    )


class ProductReviewDatabaseModel(Base):
    __tablename__ = "product_reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int]
    text: Mapped[Optional[str]]
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped[ProductDatabaseModel] = relationship(back_populates="reviews")


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

    users: Mapped[list["UserDatabaseModel"]] = relationship(
        secondary="users_roles", back_populates="roles"
    )


class UserDatabaseModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    phone_number: Mapped[Optional[str]] = mapped_column(unique=True, index=True)
    first_name: Mapped[str]
    last_name: Mapped[Optional[str]]

    roles: Mapped[list[RoleDatabaseModel]] = relationship(
        secondary="users_roles", back_populates="users"
    )

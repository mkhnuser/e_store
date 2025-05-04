import os
from typing import Optional

from sqlalchemy import String, Table, Column, ForeignKey, Numeric, MetaData
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


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    name: Mapped[str]
    price: Mapped[float] = mapped_column(Numeric())


users_roles_table = Table(
    "users_roles",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
)


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(int(os.environ["APP_ROLE_NAME_MAX_LENGTH"]))
    )
    description: Mapped[str] = mapped_column(
        String(int(os.environ["APP_ROLE_DESCRIPTION_MAX_LENGTH"]))
    )
    users: Mapped[list["User"]] = relationship(
        secondary="users_roles", back_populates="roles"
    )


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(int(os.environ["APP_USER_EMAIL_MAX_LENGTH"])), unique=True
    )
    phone_number: Mapped[Optional[str]] = mapped_column(
        String(int(os.environ["APP_USER_PHONE_NUMBER_MAX_LENGTH"])), unique=True
    )
    first_name: Mapped[str] = mapped_column(
        String(int(os.environ["APP_USER_FIRST_NAME_MAX_LENGTH"]))
    )
    last_name: Mapped[Optional[str]] = mapped_column(
        String(int(os.environ["APP_USER_LAST_NAME_MAX_LENGTH"]))
    )
    age: Mapped[Optional[int]]

    roles: Mapped[list[Role]] = relationship(
        secondary="users_roles", back_populates="users"
    )

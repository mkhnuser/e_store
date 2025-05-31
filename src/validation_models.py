import os
from typing import Optional
from pydantic import BaseModel, Field, EmailStr, PositiveInt


class UserValidationModelBase(BaseModel):
    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "examples": [
                {
                    "email": "test@email.com",
                    "password": "qwerty",
                    "phone_number": "+399000000000",
                    "first_name": "Vlad",
                    "last_name": "Mikheenko",
                    "roles": [
                        {"name": "customer", "description": "A plain customer role."}
                    ],
                }
            ]
        },
    }
    email: EmailStr = Field(
        min_length=int(os.environ["APP_USER_EMAIL_MIN_LENGTH"]),
        max_length=int(os.environ["APP_USER_EMAIL_MAX_LENGTH"]),
    )
    phone_number: Optional[str] = Field(
        min_length=int(os.environ["APP_USER_PHONE_NUMBER_MIN_LENGTH"]),
        max_length=int(os.environ["APP_USER_PHONE_NUMBER_MAX_LENGTH"]),
    )
    first_name: str = Field(
        min_length=int(os.environ["APP_USER_FIRST_NAME_MIN_LENGTH"]),
        max_length=int(os.environ["APP_USER_FIRST_NAME_MAX_LENGTH"]),
    )
    last_name: Optional[str] = Field(
        max_length=int(os.environ["APP_USER_LAST_NAME_MAX_LENGTH"])
    )


class UserValidationModelIn(UserValidationModelBase):
    password: str = Field(
        min_length=int(os.environ["APP_USER_PASSWORD_MIN_LENGTH"]),
        max_length=int(os.environ["APP_USER_PASSWORD_MAX_LENGTH"]),
    )
    roles: list["RoleValidationModelIn"] = Field(
        min_length=int(os.environ["APP_USER_MIN_NUM_OF_ROLES"]),
        max_length=int(os.environ["APP_USER_MAX_NUM_OF_ROLES"]),
    )


class UserValidationModelOut(UserValidationModelBase):
    id: PositiveInt
    roles: list["RoleValidationModelOut"] = Field(
        min_length=int(os.environ["APP_USER_MIN_NUM_OF_ROLES"]),
        max_length=int(os.environ["APP_USER_MAX_NUM_OF_ROLES"]),
    )


class ProductValidationModelBase(BaseModel):
    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Mathematical logic book",
                    "description": "A super interesting math logic book.",
                    "price": 44.99,
                    "reviews": [],
                }
            ]
        },
    }
    name: str = Field(
        min_length=int(os.environ["APP_PRODUCT_NAME_MIN_LENGTH"]),
        max_length=int(os.environ["APP_PRODUCT_NAME_MAX_LENGTH"]),
    )
    description: Optional[str] = Field(
        max_length=int(os.environ["APP_PRODUCT_DESCRIPTION_MAX_LENGTH"])
    )
    price: float = Field(
        ge=int(os.environ["APP_PRODUCT_MIN_PRICE"]),
        le=int(os.environ["APP_PRODUCT_MAX_PRICE"]),
        allow_inf_nan=False,
    )
    reviews: list["ProductReviewValidationModelOut"]


class ProductValidationModelIn(ProductValidationModelBase):
    pass


class ProductValidationModelOut(ProductValidationModelBase):
    id: PositiveInt


class ProductReviewValidationModelBase(BaseModel):
    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "examples": [
                {"rating": 5, "text": "This book is wonderful!", "product_id": 1}
            ]
        },
    }
    rating: int = Field(
        ge=os.environ["APP_PRODUCT_REVIEW_MIN_VALUE"],
        le=os.environ["APP_PRODUCT_REVIEW_MAX_VALUE"],
    )
    text: Optional[str] = Field(
        max_length=int(os.environ["APP_PRODUCT_REVIEW_TEXT_MAX_LENGTH"])
    )
    product_id: int


class ProductReviewValidationModelIn(ProductReviewValidationModelBase):
    pass


class ProductReviewValidationModelOut(ProductReviewValidationModelBase):
    id: PositiveInt


class RoleValidationModelBase(BaseModel):
    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "examples": [
                {
                    "name": "customer",
                    "description": "A plain customer role.",
                }
            ]
        },
    }
    name: str = Field(
        min_length=int(os.environ["APP_ROLE_NAME_MIN_LENGTH"]),
        max_length=int(os.environ["APP_ROLE_NAME_MAX_LENGTH"]),
    )
    description: Optional[str] = Field(
        max_length=int(os.environ["APP_ROLE_DESCRIPTION_MAX_LENGTH"])
    )


class RoleValidationModelIn(RoleValidationModelBase):
    pass


class RoleValidationModelOut(RoleValidationModelBase):
    id: PositiveInt

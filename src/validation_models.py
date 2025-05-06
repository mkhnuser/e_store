import os
from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class UserValidationModel(BaseModel):
    model_config = {"extra": "forbid"}
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
    roles: list[str] = Field(
        ge=os.environ["APP_USER_MIN_NUM_OF_ROLES"],
        le=os.environ["APP_USER_MAX_NUM_OF_ROLES"],
    )


class ProductValidationModel(BaseModel):
    model_config = {"extra": "forbid"}
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
    reviews: list["ProductReviewValidationModel"]


class ProductReviewValidationModel(BaseModel):
    model_config = {"extra": "forbid"}
    value: int = Field(
        ge=os.environ["APP_PRODUCT_REVIEW_MIN_VALUE"],
        le=os.environ["APP_PRODUCT_REVIEW_MAX_VALUE"],
    )
    text: Optional[str] = Field(
        max_length=int(os.environ["APP_PRODUCT_REVIEW_TEXT_MAX_LENGTH"])
    )
    product_id: int


class RoleValidationModel(BaseModel):
    model_config = {"extra": "forbid"}
    name: str = Field(
        min_length=int(os.environ["APP_ROLE_NAME_MIN_LENGTH"]),
        max_length=int(os.environ["APP_ROLE_NAME_MAX_LENGTH"]),
    )
    description: Optional[str] = Field(
        max_length=int(os.environ["APP_ROLE_DESCRIPTION_MAX_LENGTH"])
    )

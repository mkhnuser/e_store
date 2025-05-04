import os
from pydantic import BaseModel
from pydantic import Field


class CustomerModel(BaseModel):
    name: str = Field(
        min_length=int(os.environ["APP_CUSTOMER_NAME_MIN_LENGTH"]),
        max_length=int(os.environ["APP_CUSTOMER_NAME_MAX_LENGTH"]),
    )
    age: int = Field(
        ge=int(os.environ["APP_CUSTOMER_MIN_AGE"]),
        le=int(os.environ["APP_CUSTOMER_MAX_AGE"]),
    )


class ProductModel(BaseModel):
    name: str = Field(
        min_length=int(os.environ["APP_PRODUCT_NAME_MIN_LENGTH"]),
        max_length=int(os.environ["APP_PRODUCT_NAME_MAX_LENGTH"]),
    )
    price: float = Field(
        ge=int(os.environ["APP_PRODUCT_MIN_PRICE"]),
        le=int(os.environ["APP_PRODUCT_MAX_PRICE"]),
        allow_inf_nan=False,
    )


class SellerModel(BaseModel):
    name: str = Field(
        min_length=int(os.environ["APP_SELLER_NAME_MIN_LENGTH"]),
        max_length=int(os.environ["APP_SELLER_NAME_MAX_LENGTH"]),
    )
    age: int = Field(
        ge=int(os.environ["APP_SELLER_MIN_AGE"]),
        le=int(os.environ["APP_SELLER_MAX_AGE"]),
    )

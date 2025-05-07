import os

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .db import get_db_session
from .validation_models import (
    UserValidationModelIn,
    UserValidationModelOut,
    ProductValidationModelIn,
    ProductValidationModelOut,
)


###### ROUTERS
products_router = APIRouter(prefix=os.environ["APP_ROUTERS_PRODUCTS_PREFIX"])
users_router = APIRouter(prefix=os.environ["APP_ROUTERS_USERS_PREFIX"])


###### USERS API ENDPOINTS
@users_router.get(os.environ["APP_API_PATHS_USERS_GET_ALL_USERS"])
async def get_all_users() -> list[UserValidationModelOut]:
    return []


@users_router.get(os.environ["APP_API_PATHS_USERS_GET_USER_BY_ID"])
async def get_user_by_id(user_id: int) -> UserValidationModelOut:
    return {}


@users_router.post(os.environ["APP_API_PATHS_USERS_POST_USER"])
async def post_user(user_model: UserValidationModelIn) -> UserValidationModelOut:
    return {}


###### PRODUCTS API ENDPOINTS
@products_router.get(os.environ["APP_API_PATHS_PRODUCTS_GET_ALL_PRODUCTS"])
async def get_all_products() -> list[ProductValidationModelOut]:
    return []


@products_router.get(os.environ["APP_API_PATHS_PRODUCTS_GET_PRODUCT_BY_ID"])
async def get_product_by_id(product_id: int) -> ProductValidationModelOut:
    return {}


@products_router.post(os.environ["APP_API_PATHS_PRODUCTS_POST_PRODUCT"])
async def post_product(
    product_model: ProductValidationModelIn,
) -> ProductValidationModelOut:
    return {}

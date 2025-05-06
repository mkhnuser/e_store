import os

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .db import get_db_session
from .validation_models import UserValidationModel, ProductValidationModel


###### ROUTERS
products_router = APIRouter(prefix=os.environ["APP_ROUTERS_PRODUCTS_PREFIX"])
users_router = APIRouter(prefix=os.environ["APP_ROUTERS_USERS_PREFIX"])


###### USERS API ENDPOINTS
@users_router.get(os.environ["APP_API_PATHS_USERS_GET_ALL_USERS"])
async def get_all_users() -> list[UserValidationModel]:
    return []


@users_router.get(os.environ["APP_API_PATHS_USERS_GET_USER_BY_ID"])
async def get_user_by_id(user_id: int):
    return {}


@users_router.post(os.environ["APP_API_PATHS_USERS_POST_USER"])
async def post_user(user_model: UserValidationModel) -> UserValidationModel:
    return user_model


###### PRODUCTS API ENDPOINTS
@products_router.get(os.environ["APP_API_PATHS_PRODUCTS_GET_ALL_PRODUCTS"])
async def get_all_products() -> list[ProductValidationModel]:
    return []


@products_router.get(os.environ["APP_API_PATHS_PRODUCTS_GET_PRODUCT_BY_ID"])
async def get_product_by_id(product_id: int):
    return {}


@products_router.post(os.environ["APP_API_PATHS_PRODUCTS_POST_PRODUCT"])
async def post_product(
    product_model: ProductValidationModel,
) -> ProductValidationModel:
    return product_model

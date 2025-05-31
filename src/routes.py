import os
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Path
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from .db import get_db_session
from .validation_models import (
    UserValidationModelIn,
    UserValidationModelOut,
    ProductValidationModelIn,
    ProductValidationModelOut,
)
from . import controllers


######
###### ROUTERS
######
products_router = APIRouter(
    prefix=os.environ["APP_ROUTERS_PRODUCTS_PREFIX"],
    tags=[os.environ["APP_ROUTERS_PRODUCTS_TAG"]],
)
users_router = APIRouter(
    prefix=os.environ["APP_ROUTERS_USERS_PREFIX"],
    tags=[os.environ["APP_ROUTERS_USERS_TAG"]],
)


######
###### PARAMETERS.
######
class UsersPaginationParameters(BaseModel):
    limit: int = Field(
        int(
            os.environ["APP_API_PATHS_USERS_GET_USERS_QUERY_PARAM_LIMIT_DEFAULT_VALUE"]
        ),
        ge=int(os.environ["APP_API_PATHS_USERS_GET_USERS_QUERY_PARAM_LIMIT_MIN_VALUE"]),
        le=int(os.environ["APP_API_PATHS_USERS_GET_USERS_QUERY_PARAM_LIMIT_MAX_VALUE"]),
    )
    offset: int = Field(
        int(
            os.environ["APP_API_PATHS_USERS_GET_USERS_QUERY_PARAM_OFFSET_DEFAULT_VALUE"]
        ),
        ge=int(
            os.environ["APP_API_PATHS_USERS_GET_USERS_QUERY_PARAM_OFFSET_MIN_VALUE"]
        ),
    )


######
###### USERS API ENDPOINTS
######
@users_router.get(
    os.environ["APP_API_PATHS_USERS_GET_USERS"],
    response_model=list[UserValidationModelOut],
)
async def get_users(
    s: Annotated[AsyncSession, Depends(get_db_session)],
    params: Annotated[UsersPaginationParameters, Depends()],
):
    try:
        return [
            user
            async for user in controllers.get_users(
                s,
                params.limit,
                params.offset,
            )
        ]
    except Exception as e:
        # TODO: IMPLEMENT LOGGING AND GRANULAR ERROR HANDLING.
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@users_router.get(
    os.environ["APP_API_PATHS_USERS_GET_USER_BY_ID"],
    response_model=UserValidationModelOut,
)
async def get_user_by_id(
    s: Annotated[AsyncSession, Depends(get_db_session)],
    user_id: Annotated[
        int,
        Path(
            title="User's ID.",
            ge=int(
                os.environ[
                    "APP_API_PATHS_USERS_GET_USER_BY_ID_PATH_PARAM_USER_ID_MIN_VALUE"
                ]
            ),
        ),
    ],
):
    try:
        return await controllers.get_user_by_id(s, user_id)
    except Exception as e:
        # TODO: IMPLEMENT LOGGING AND GRANULAR ERROR HANDLING.
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@users_router.post(
    os.environ["APP_API_PATHS_USERS_POST_USER"],
    response_model=UserValidationModelOut,
)
async def post_user(
    s: Annotated[AsyncSession, Depends(get_db_session)],
    user_model: UserValidationModelIn,
):
    try:
        return await controllers.post_user(s, user_model)
    except Exception as e:
        # TODO: IMPLEMENT LOGGING AND GRANULAR ERROR HANDLING.
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


######
###### PRODUCTS API ENDPOINTS
######
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

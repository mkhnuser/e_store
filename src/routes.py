from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .db import get_db_session
from .validation_models import UserValidationModel, ProductValidationModel


###### ROUTERS
products_router = APIRouter(prefix="/api/v1/products")
users_router = APIRouter(prefix="/api/v1/users")


###### USERS API ENDPOINTS
@users_router.get("/")
async def get_all_users(db_session: Session = Depends(get_db_session)):
    return {"customers": True}


@users_router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    return {"user_id": user_id}


@users_router.post("/")
async def post_user(user_model: UserValidationModel):
    return user_model


###### PRODUCTS API ENDPOINTS
@products_router.get("/")
async def get_all_products():
    return {"products": "all"}


@products_router.get("/{product_id}")
async def get_product_by_id(product_id: int):
    return {"product_id": product_id}


@products_router.post("/")
async def post_product(product_model: ProductValidationModel):
    return product_model

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .db import get_db_session
from .validation_models import CustomerModel, ProductModel, SellerModel


customers_router = APIRouter(prefix="/api/v1/customers")


@customers_router.get("/")
async def get_all_customers(db_session: Session = Depends(get_db_session)):
    return {"customers": True}


@customers_router.get("/{customer_id}")
async def get_customer_by_id(customer_id: int):
    return {"customer_id": customer_id}


@customers_router.post("/")
async def post_customer(customer_model: CustomerModel):
    return customer_model


products_router = APIRouter(prefix="/api/v1/products")


@products_router.get("/")
async def get_all_products():
    return {"products": "all"}


@products_router.get("/{product_id}")
async def get_product_by_id(product_id: int):
    return {"product_id": product_id}


@products_router.post("/")
async def post_product(product_model: ProductModel):
    return product_model


sellers_router = APIRouter(prefix="/api/v1/sellers")


@sellers_router.get("/")
async def get_all_sellers():
    return {"sellers": "all"}


@sellers_router.get("/{seller_id}")
async def get_seller_by_id(seller_id: int):
    return {"seller_id": seller_id}


@sellers_router.post("/")
async def post_seller(seller_model: SellerModel):
    return seller_model

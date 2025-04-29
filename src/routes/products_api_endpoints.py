from fastapi import APIRouter
from ..pydantic_models.products_models import ProductModel


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

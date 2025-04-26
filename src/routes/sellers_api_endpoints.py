from fastapi import APIRouter
from ..models.sellers_models import SellerModel


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

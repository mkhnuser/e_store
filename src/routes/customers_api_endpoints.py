from fastapi import APIRouter
from ..models.customers_models import CustomerModel


customers_router = APIRouter(prefix="/api/v1/customers")


@customers_router.get("/")
async def get_all_customers():
    return {"customers": "all"}


@customers_router.get("/{customer_id}")
async def get_customer_by_id(customer_id: int):
    return {"customer_id": customer_id}


@customers_router.post("/")
async def post_customer(customer_model: CustomerModel):
    return customer_model

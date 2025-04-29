from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db.db import get_db_session
from ..pydantic_models.customers_models import CustomerModel
from ..controllers import customers_controllers


customers_router = APIRouter(prefix="/api/v1/customers")


@customers_router.get("/")
async def get_all_customers(db_session: Session = Depends(get_db_session)):
    return {"customers": customers_controllers.get_all_customers(db_session)}


@customers_router.get("/{customer_id}")
async def get_customer_by_id(customer_id: int):
    return {"customer_id": customer_id}


@customers_router.post("/")
async def post_customer(customer_model: CustomerModel):
    return customer_model

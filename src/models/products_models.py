from pydantic import BaseModel
from pydantic import Field


class ProductModel(BaseModel):
    name: str = Field(min_length=1, max_length=64)
    price: float = Field(ge=0, le=10**6, allow_inf_nan=False)

from pydantic import BaseModel
from pydantic import Field


class CustomerModel(BaseModel):
    name: str = Field(min_length=1, max_length=64)
    age: int = Field(ge=0, le=128)

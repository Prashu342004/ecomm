from pydantic import BaseModel
from pydantic import ConfigDict

class productCreate(BaseModel):
    product_name:str
    price: float
    quantity_available: int


class ProductResponse(BaseModel):

    product_id: int
    product_name: str
    quantity_available: int

    model_config = ConfigDict(from_attributes=True)

class productUpdate(BaseModel):
    product_name: str
    price: float
    quantity_available: int


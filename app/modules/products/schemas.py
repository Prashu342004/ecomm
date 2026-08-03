from pydantic import BaseModel
from uuid import UUID

class productCreate(BaseModel):
    name:str
    price: float
    quantity: int
    image : str|None = None


class ProductResponse(BaseModel):
    id: UUID
    name : str
    price: float
    quantity : int
    image : str|None = None

    model_config = {
        "from_attributes": True
    }

class productUpdate(BaseModel):
    name: str
    price: float
    quantity: int
    image : str|None = None


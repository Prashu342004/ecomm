from pydantic import BaseModel

class productCreate(BaseModel):
    name:str
    price: float
    quantity: int


class ProductResponse(BaseModel):
    id: int
    name : str
    price: float
    quantity : int

    model_config = {
        "from_attributes": True
    }

class productUpdate(BaseModel):
    name: str
    price: float
    quantity: int


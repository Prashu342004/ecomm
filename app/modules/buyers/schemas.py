from pydantic import BaseModel, Field


class OrderProduct(BaseModel):
    product_name: str
    quantity: int


class BuyProductRequest(BaseModel):
    buyer_id: int
    
    shipping_address: str
    products: list[OrderProduct]


class UpdateQuantityRequest(BaseModel):

    name: str

    qty: int = Field(gt=0)


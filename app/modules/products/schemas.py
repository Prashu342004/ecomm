from pydantic import BaseModel

class product(BaseModel):
    id : int
    seller_id : int
    name : str
    price : float
    quantity : int
    image : str
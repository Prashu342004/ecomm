from fastapi import FastAPI
from pydantic import BaseModel


class product(BaseModel):
    product_id : int
    product_name : str
    product_quantity : int
    product_price : int
    product_image : str





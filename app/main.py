from fastapi import FastAPI

from app.modules.products.router import router as product_router
from app.modules.seller.router import router as seller_router

app = FastAPI()

app.include_router(product_router)

app.include_router(seller_router)
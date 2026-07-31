from fastapi import FastAPI

from app.modules.products.router import router as product_router
from app.modules.seller.router import router as seller_router
from app.modules.buyers.routers import router as buyer_router

app = FastAPI()
from app.databases.database import engine, Base
from app.modules.buyers.models import Order, OrderItems
from app.databases.models import Product

Base.metadata.create_all(bind=engine)

# app.include_router(product_router)

# app.include_router(seller_router)

app.include_router(
    buyer_router,
    tags = ["Buyer Dashboard"]
)
from fastapi import FastAPI
from app.database.session import engine
from app.modules.products.router import router as product_router
from app.modules.products.models import Base


Base.metadata.create_all(bind = engine)
app = FastAPI()

app.include_router(product_router)
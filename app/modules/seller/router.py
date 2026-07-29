# here we will solve http requests
from fastapi import APIRouter
from app.modules.products.schemas import product
from .service import service


router = APIRouter(
    prefix="/seller"
)


@router.post("/products")
def create_product(product: product):
    return service.create_product(product)

@router.get("/products")
def get_my_products():
    return service.get_products()
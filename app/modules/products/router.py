from fastapi import APIRouter
from .service import service

router  = APIRouter()


@router.get("/products")
def get_products():
    return service.get_products()

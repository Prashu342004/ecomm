from fastapi import APIRouter
# from app.databases.database import engine , Base ,SessionLocal
# from app.databases.models import Product
from app.databases.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session


from . import models

# Base.metadata.create_all(bind = engine)


from .schemas import (
    BuyProductRequest,
    UpdateQuantityRequest
)

from .services import (
    view_products,
    buy_product,
    update_quantity
)

router = APIRouter()
print(router)


@router.get("/view-products")
def get_products(
    db : Session = Depends(get_db)
):
    

    return view_products(db)


# @router.post("/buy-product")
# def buy(request: BuyProductRequest,
#         db : Session = Depends(get_db)
#         ):

#     return buy_product(
#         db,
#         request.name,
#         request.qty
#     )


@router.post("/buy-product")
def buy(
    request: BuyProductRequest,
    db: Session = Depends(get_db)
):
    return buy_product(
        db=db,
        request=request
    )


@router.put("/update-quantity")
def update(request: UpdateQuantityRequest,
           db : Session = Depends(get_db)
           ):

    return update_quantity(
        db,
        request.name,
        request.qty
    )















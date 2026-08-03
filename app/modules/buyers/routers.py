from fastapi import APIRouter
from app.databases.session import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import Form
from . import models


from .schemas import (
    BuyProductRequest,
    UpdateQuantityRequest
)

from .services import (
    view_products,
    buy_product,
    update_quantity,
    view_product_by_name
)

router = APIRouter()
print(router)


@router.get("/view-products")
def get_products(
    db : Session = Depends(get_db)
):
    

    return view_products(db)



@router.get("/view-products_byName/{product_name}")
def get_products(
    product_name :  str ,
    db : Session = Depends(get_db)
    
):
  
    return view_product_by_name(db , product_name)




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















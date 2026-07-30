from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from . import service,schemas

router = APIRouter()

@router.post("/products", response_model= schemas.ProductResponse)
def create_product(
    product: schemas.productCreate,
    db: Session = Depends(get_db)
):
    return service.create_product(db,product)


@router.get("/products",response_model= list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return service.get_products(db)


@router.get("/products/{product_id}",response_model = schemas.ProductResponse)
def get_product(product_id: int ,
                db: Session = Depends(get_db)
    ):
    product = service.get_product(db,product_id)
    if product is None:
        raise HTTPException(
            status_code= 404,
            details= "product not found"
        )
    return product


@router.put(
    "/products/{product_id}",
    response_model=schemas.ProductResponse
)
def update_product(
    product_id : int,
    product: schemas.productUpdate,
    db: Session = Depends(get_db)
):
    updated = service.update_product(
        db,
        product_id,
        product
    )
    if updated is None:
        raise HTTPException(
            status_code= 404,
            detail= "product not found"
        )
    return updated

@router.delete(
    "/products",response_model= schemas.ProductResponse
)
def delete_product(
    product_id :int,
    product: schemas.ProductResponse,
    db: Session = Depends(get_db)
):
    deleted = service.delete_product(db,product_id,product)
    if deleted is None:
        raise HTTPException(
            status_code= 404,
            detail= "product not found"
        )
    return deleted
    
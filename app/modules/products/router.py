from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.databases.session import get_db
from . import schemas, service

router = APIRouter()


@router.post("/products", response_model=schemas.ProductResponse)
def create_product(product: schemas.productCreate,db: Session = Depends(get_db)):
    return service.create_product(db, product)


@router.get("/products", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return service.get_products(db)


@router.get("/products/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return service.get_product(db, product_id)


@router.put("/products/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int,product: schemas.productUpdate,db: Session = Depends(get_db)):
    return service.update_product(db, product_id, product)


@router.delete("/products/{product_id}", response_model=schemas.ProductResponse)
def delete_product(product_id: int,db: Session = Depends(get_db)):
    return service.delete_product(db, product_id)



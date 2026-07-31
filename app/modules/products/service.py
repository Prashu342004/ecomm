from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import repository, schemas


def create_product(db: Session,product: schemas.productCreate):
    return repository.create_product(db, product)


def get_products(db: Session):
    return repository.get_products(db)


def get_product(db: Session,product_id: int):
    product = repository.get_product(db, product_id)

    if product is None:
        raise HTTPException(status_code=404,detail="Product not found")

    return product



def update_product(db: Session,product_id: int,product: schemas.productUpdate):

    db_product = repository.get_product(db, product_id)

    if db_product is None:
        raise HTTPException(status_code=404,detail="Product not found")

    return repository.update_product(db,db_product, product)



def delete_product(db: Session,product_id: int):
    product = repository.get_product(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return repository.delete_product(db,product)
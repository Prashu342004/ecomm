from sqlalchemy.orm import Session

from . import models,schemas

def create_product(db: Session, product: schemas.productCreate):
    db_product = models.Product(
        name = product.name,
        price = product.price,
        quantity = product.quantity
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

def get_products(db: Session):
    return db.query(models.Product).all()


def get_product(db: Session , product_id: int):
    return(
        db.query(models.Product)
        .filter(models.Product.id == product_id)
        .first()
    )

def update_product(
        db: Session,
        product_id:int,
        product: schemas.productUpdate):
    db_product = (
        db.query(models.Product)
        .filter(models.Product.id == product_id)
        .first()
    )

    if db_product is None:
        return None
    db_product.name = product.name
    db_product.price = product.price
    db_product.quantity = product.quantity

    db.commit()
    db.refresh(db_product)

    return  db_product


def delete_product(
        db: Session,
        product_id : int,
        product: schemas.ProductResponse
):
    product = (
        db.query(models.Product)
        .filter(models.Product.id == product_id)
        .first()
    )
    if product == None:
        return None

    db.delete(product)
    db.commit()

    return product

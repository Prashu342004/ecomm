from sqlalchemy.orm import Session
from . import models, schemas
from app.modules.products.models import Product


def create_product(db: Session,  product: schemas.productCreate):
    db_product = models.Product(product_name=product.product_name, price=product.price, quantity_available=product.quantity_available )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


# def get_products(db: Session):
#     return db.query(models.Product).all()

def get_all_products(db : Session):
    return db.query(Product).all()

def get_product_by_name(db: Session, name: str):

    return (
        db.query(Product)
        .filter(Product.product_name == name)
        .first()
    )


def get_product(db: Session, product_id: int): #merge it with get product use none
    return (db.query(models.Product).filter(models.Product.product_id == product_id).first())


def update_product(db: Session,db_product: models.Product,product: schemas.productUpdate):
    db_product.product_name = product.product_name
    db_product.price = product.price
    db_product.quantity_available = product.quantity_available

    db.commit()
    db.refresh(db_product)

    return db_product


def delete_product(db: Session,product: models.Product):
    db.delete(product)
    db.commit()

    return product
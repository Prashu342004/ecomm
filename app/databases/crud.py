from app.databases.database import db
from app.databases.models import Product

def insert_product():

    product = Product(
        product_name="Laptop",
        price=50000,
        quantity_available=10
    )

    db.add(product)


    db.commit()


    return product

insert_product()
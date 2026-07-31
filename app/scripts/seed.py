from app.databases.database import SessionLocal
from app.databases.models import Product
from app.modules.buyers.models import OrderItems , Order

db = SessionLocal()


    
product1 = Product(
    product_name="Shirts",
    price=300,
    quantity_available=10
)
product2 = Product(
    product_name="Sunglasses",
    price=1000,
    quantity_available=20
)
product3 = Product(
    product_name="Footwear",
    price=50000,
    quantity_available=30
)

products = [
    product1,
    product2,
    product3

]

db.add_all(products)

db.commit()

print("Added successfully")
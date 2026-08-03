# from app.databases.database import db 

from app.modules.products.models import Product
from sqlalchemy.orm import Session
from app.modules.buyers.models import Order , OrderItems
from datetime import datetime

# def get_all_products(db : Session):
#     return db.query(Product).all()


# def get_product_by_name(db: Session, name: str):

#     return (
#         db.query(Product)
#         .filter(Product.product_name == name)
#         .first()
#     )



def create_order(
    db: Session,
    buyer_id: int,
    shipping_address: str,
    total_amount: float
):
    order = Order(buyer_id=buyer_id,
    
            order_date=datetime.now(),
    
            status="Placed",
    
            payment_status="Pending",
    
            shipping_address=shipping_address,
    
            Total_Amount=total_amount)
    db.add(order)
    db.flush()
    return  order

def create_order_item(
    db,
    order_id: int,
    product_id: int,
    quantity: int,
    price: float
):

    order_item = OrderItems(

        order_id=order_id,

        product_id=product_id,

        quantity=quantity,

        price=price

    )

    db.add(order_item)

    return order_item  

def update_product_stock(
    db,
    product: Product,
    quantity: int
):

    product.quantity_available -= quantity

    return product 
    

    
def update_product_quantity( db : Session  , product: dict, qty: int):

    product.quantity_available -= qty
    db.commit()
    db.refresh(product)
    

    return product
from app.databases.database import Base 
from app.databases.models import Product
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = "Orders"
    order_id = Column(Integer , primary_key = True , autoincrement = True)
    buyer_id = Column(Integer , nullable = False)
    order_date = Column(DateTime , nullable = False)
    status = Column(String(100) , default = "Placed")
    payment_status = Column(String(100) , default = "Pending")
    shipping_address = Column(String(100) , nullable = False)
    Total_Amount =  Column(Float, nullable = False)

    order_items = relationship(
        "OrderItems",
        back_populates="order"
    )
    


class OrderItems(Base):
    __tablename__ = "Order_items"
    order_item_id = Column(Integer , primary_key = True , autoincrement = True)
    order_id = Column(Integer , ForeignKey("Orders.order_id") , nullable =False)
    product_id = Column(Integer , ForeignKey("Products_available.product_id"), nullable =False)
    quantity = Column(Integer , default = 1 , nullable = False)
    price = Column(Float , nullable = False)

    order = relationship(
        "Order",
        back_populates="order_items"
    )

    product = relationship(
        "Product",
        back_populates="order_items"
    )
        

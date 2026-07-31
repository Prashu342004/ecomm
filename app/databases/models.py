from .database import Base 
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "Products_available"
    product_id = Column(Integer , primary_key = True , autoincrement = True)
    product_name = Column(String(100) , nullable = False)
    price = Column(Float)
    quantity_available = Column(Integer , nullable = False )
    order_items = relationship(
        "OrderItems",
        back_populates="product"
    )
    



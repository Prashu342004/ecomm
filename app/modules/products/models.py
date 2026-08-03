from sqlalchemy import Column, Integer, String, Numeric
from app.database.base import Base
from uuid import UUID


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer,primary_key=True, index = True) # use uuid here
    name = Column(String(20) , nullable= False)
    price = Column(Numeric(10,2), nullable = False)
    quantity = Column(Integer, default= 0)
    image = Column(String(255),nullable= True)

    

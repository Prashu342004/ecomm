from sqlalchemy import Column, Integer, String, Float
from app.database.session import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer,primary_key=True, index = True) # use uuid here
    name = Column(String , nullable= False)
    price = Column(Float, nullable = False)
    quantity = Column(Integer, default= 0)

    

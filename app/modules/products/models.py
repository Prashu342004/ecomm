from sqlalchemy import Column, Integer, String, Numeric
from app.database.base import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key= True, default= uuid.uuid4)
    name = Column(String(20) , nullable= False)
    price = Column(Numeric(10,2), nullable = False)
    quantity = Column(Integer, default= 0)
    image = Column(String(255),nullable= True)

    

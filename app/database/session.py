from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
import os
from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")



engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(
    autoflush= False,
    autocommit = False,
    bind = engine
)

class Base(DeclarativeBase):
    pass

def get_db():  #use exception handling here
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
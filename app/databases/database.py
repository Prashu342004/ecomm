DATABASE_URL =  "postgresql+psycopg2://postgres:root@localhost:5432/product_db"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

# SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


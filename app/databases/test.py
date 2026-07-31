# from fastapi import FastAPI
# from app.databases.database import engine , Base ,SessionLocal
# app = FastAPI()
# from app.databases.models import Product

# from . import models

# Base.metadata.create_all(bind = engine)
# @app.get('/')
# def home():
#     return{
#         "Message" : "Table created"
#     }

# @app.get("/users-list")
# def get_product():

#     def get_db():

#         db = SessionLocal()

#         try:
#             yield db

#         finally:
#             db.close()

#         products = db.query(Product).all()

#         db.close()

#         return products

# print("TEST FILE EXECUTED")

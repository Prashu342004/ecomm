# from fastapi import APIRouter
# from fastapi import Form
# from src.db import products
# from typing import Annotated
# from fastapi import HTTPException
# router = APIRouter()

# @router.get("/View_product")
# def view_items():
#     return products

# @router.post("/Buy_product")
# def buy_items(
#     name = Annotated[str , Form(min_length = 8 , description = "Product name")],
#     qty: Annotated[int, Form(gt=0)] = 1 

# ):
#     for product in products:
        
#         if product["name"] == name :
            
#             if qty <=  product["qty"] :
#                 product["qty"] -= qty
                

                 

#                 return{
#                     "status" : "Order placed successfully",
#                     "Product_name" : name,
#                     "Price" : product["price"],
#                     "quantity" :  qty,
#                     "available_Stock" : product["qty"]
#                 }
#             else:
#                  raise HTTPException(
#                                  status_code=404,
#                                  detail="out of stock"
#                              )

#     raise HTTPException(
#                     status_code=404,
#                     detail="Product not found"
#                 )

# @router.put("/Update_Quantity{product_quantity}")
# def update_quantity(
#     name = Annotated[str , Form(min_length = 8 , description = "Product name")],
#     qty: Annotated[int, Form(gt=0)] = 1 
    
#     ):
#         for product in products:
            
#             if product["name"] == name :
                
#                 if qty <=  product["qty"] :
#                     product["qty"] -= qty
                    
    
                     
    
#                     return{
#                         "status" : "quantity updated successfully",
#                         "Product_name" : name,
#                         "Price" : product["price"],
#                         "quantity" :  qty,
#                         "available_Stock" : product["qty"]
#                     }
#                 else:
#                      raise HTTPException(
#                                      status_code=404,
#                                      detail="Out of stock"
#                                  )
#         raise HTTPException(
#             status_code=404,
#             detail="Product not found"
#         )




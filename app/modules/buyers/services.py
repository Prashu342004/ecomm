from fastapi import HTTPException
# from .models import Product
from sqlalchemy.orm import Session
from app.modules.buyers.models import Order , OrderItems
from .schemas import BuyProductRequest
from .schemas import UpdateQuantityRequest

from .repository import (
    get_all_products,
    get_product_by_name,
    
    create_order,
    create_order_item,
    update_product_stock
)


def buy_product(
    db: Session,
    request: BuyProductRequest
):  
    total = 0
    buyer_id = request.buyer_id
    shipping_address = request.shipping_address

    for item in request.products:

        product = get_product_by_name(
            db,
            item.product_name
        )

        if product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        if item.quantity > product.quantity_available:
            raise HTTPException(
                status_code=400,
                detail="Out of stock"
            )

        

        total += product.price * item.quantity

    try:

        order = create_order(
            db=db,
            buyer_id=buyer_id,
            shipping_address=shipping_address,
            total_amount=total
        )

        create_order_item(
            db=db,
            order_id=order.order_id,
            product_id=product.product_id,
            quantity=item.quantity,
            price=product.price
        )

        update_product_stock(
            db=db,
            product=product,
            quantity=item.quantity
        )

        db.commit()

        db.refresh(order)
        db.refresh(product)

        return {
            "message": "Order placed successfully",
            "order_id": order.order_id,
            "product_name": product.product_name,
            "price": product.price,
            "quantity_ordered": item.quantity,
            "total_amount": total,
            "available_stock": product.quantity_available
        }

    except Exception:

        db.rollback()
        raise


def view_products(db: Session):

    return get_all_products(db)




def update_quantity(db : Session , request = UpdateQuantityRequest):

    total = 0
    buyer_id = request.buyer_id
    shipping_address = request.shipping_address

    for item in request.products:

        product = get_product_by_name(
            db,
            item.product_name
        )

        if product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        if item.quantity > product.quantity_available:
            raise HTTPException(
                status_code=400,
                detail="Out of stock"
            )

        

        total += product.price * item.quantity

    try:

    
        order = create_order_item(
            db=db,
            order_id=order.order_id,
            product_id=product.product_id,
            quantity=item.quantity,
            price=product.price
        )

        update_product_stock(
            db=db,
            product=product,
            quantity=item.quantity
        )

        db.commit()

        db.refresh(order)
        db.refresh(product)

        return {
            "message": "Quantity updated successfully",
            "order_id": order.order_id,
            "product_name": product.product_name,
            "price": product.price,
            "quantity_ordered": item.quantity,
            "total_amount": total,
            "available_stock": product.quantity_available
        }

    except Exception:

        db.rollback()
        raise



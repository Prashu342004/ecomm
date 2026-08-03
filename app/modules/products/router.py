from fastapi import APIRouter, Depends, File, UploadFile, Form
from sqlalchemy.orm import Session
from app.database.session import get_db
from . import schemas, service
from uuid import UUID



router = APIRouter()


@router.post("/products", response_model=schemas.ProductResponse)
def create_product(
    name: str = Form(...),
    price: float = Form(...),
    quantity: int = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    product = schemas.productCreate(
        name=name,
        price=price,
        quantity=quantity
    )

    return service.create_product(db, product, image)



@router.get("/products", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return service.get_products(db)


@router.get("/products/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: UUID, db: Session = Depends(get_db)):
    return service.get_product(db, product_id)


@router.put("/products/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: UUID,product: schemas.productUpdate,db: Session = Depends(get_db)):
    return service.update_product(db, product_id, product)


@router.delete("/products/{product_id}", response_model=schemas.ProductResponse)
def delete_product(product_id: UUID,db: Session = Depends(get_db)):
    return service.delete_product(db, product_id)





# @router.post("/uploadTest")
# def upload_file(image: UploadFile = File(...)):
#     return {
#         "filename" : image.filename,
#         "content_type": image.content_type,
#         "class": str(type(image)),
#         "headers": dict(image.headers)
#     }



#    Here we are uploading file as uuid name.
# @router.post("/uploadTest") 
# def upload_file(image: UploadFile = File(...)):
#     extension = os.path.splitext(image.filename)[1]
#     full_name = f"{uuid.uuid4()}{extension}"    
#     with open(f"uploads/{full_name}", "wb") as buffer:
#         shutil.copyfileobj(image.file,buffer)
#     return {
#         "message": "file uploaded sucessfully"
#     }
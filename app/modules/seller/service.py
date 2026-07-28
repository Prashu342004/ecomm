#here we will write business logic
from app.modules.products.repository import repository

class productservice:

    def create_product(self,data):

        product = {
        "id": data.id,
        "seller_id": data.seller_id,
        "name": data.name,
        "price": data.price,
        "quantity": data.quantity,
        "image": data.image,
    }

        repository.create(product)

        return data
    def get_products(self):
        return repository.get_all()
    

    
service = productservice()



from .models import products

class ProductRepository:

    def create(self,product):
        products.append(product)

    def get_all(self):
        return products

    def get_by_id(self,product_id):
        for product in products:
            if product["id"] == product_id:
                return product

        return None
    

repository = ProductRepository()
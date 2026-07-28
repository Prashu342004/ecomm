from .repository import repository

class productservice:

    def get_products(self):
        return repository.get_all()
    

    
service = productservice()
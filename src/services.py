


@app.get("/")
def root():
    return {"message":"Welcome to our ecomm platform"}


@app.get("/products")
def get_products():
    return products

@app.post("/products")
def add_products(product : product):
    products.append(product)
    return product

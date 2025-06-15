from core.file_manager import read


def show_products():
    products = read(filename="products")
    if products:
        for product in  products:
            print(f"ID: {product[0]} {product[1]}\t{product[2]}\t{product[3]}")
    
    else:
        print("No products")



def get_product(product_id):
    prooducts = read(filename="products")
    for product in prooducts:
        if product[0] == product_id:
            return product
        
    return False
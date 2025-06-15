from core.utils import get_next_id
from core.file_manager import append, read, writerows



def add_product():
    name = input("Enter the name of the product: ")
    price = input("Enter the product price : ")
    quantity = input("Enter the product quantity: ")
    
    product_id = get_next_id(filename="products")
    append(filename="products", data=[product_id, name ,price, quantity])
    print("The product was added successfully ✅")


def delete_product():
    product_id = input("Enter the product id: ")
    products = read(filename="products")
    
    new_product = []
    for product in products:
        if product[0] != product_id:
            new_product.append(product)
    products = new_product
    writerows(filename="products", data=products)
    print("Successfully deleted ✅")


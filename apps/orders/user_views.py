from apps.auth.utils import get_active_user
from apps.products.user_views import show_products, get_product
from core.utils import get_next_id
from core.file_manager import append, read, writerows
from datetime import datetime

def order_product():
    user = get_active_user()
    
    show_products()
    product_id = input("Enter the product id: ")
    product = get_product(product_id)
    while not product:
        print("Product id not found")
        product_id = input("Enter the product id: ")
        product = get_product(product_id)
        
    quantity = input("Enter the quantity: ")
    
    while int(product[-1]) < int(quantity):
        print("not enough product")
        quantity = input("Enter the quantity: ")
    
    created_at = datetime.now()
    next_id = get_next_id(filename="orders")
    
    data = [next_id,product[1], product[2], quantity, user[0], user[2], created_at]
    append(filename="orders", data=data)
    
    products = read(filename="products") 
    for index, p in enumerate(products):
        if p[0] == product_id:
            products[index][-1] = int(products[index][-1]) - int(quantity)
            writerows(filename="products", data=products)
            print("Order is created ✅")
            return 



def show_my_orders():
    user = get_active_user()
    orders = read(filename="orders")
    
    for order in orders:
        if order[-3] == user[0]:
            print(f"ID: {order[0]} {order[1]}\t{int(order[2]) * int(order[3])} USD")


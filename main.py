from apps.auth.views import register, login, logout
from apps.products import admin_views
from apps.products import user_views
from apps.orders import admin_views
from apps.orders import user_views
from apps.auth import views


def auth_menu():
    
    print("""
        ╔═════════════════════════╗
        ║       AUTH MENU         ║
        ╠═════════════════════════╣
        ║   1. Register           ║
        ║   2. Login              ║
        ║   3. Logout             ║
        ╚═════════════════════════╝

        """)

    choice = input("Enter your choice: ")
    
    if choice == "1":
        if register():
            print("Successfully registered ✅")
        else:
            print("Something went wrong")
    elif choice == "2":
        result = login()
        if result == "admin":
            print("Welcome my owner")
            return admin_menu() 
        elif result == "user":
            return user_menu()
        else:
            return login()
    elif choice == "3":
        print("Good bye :)")
        return None
    else:
        print("Invalid choice")
    return auth_menu()


def admin_menu():
    print("""
        ==================================================
                                🛠️                          
                    🔸 A D M I N   M E N U 🔸     
                                🛠️                          
        ==================================================
        
                [1] ➤ 📦  Add product                
                [2] ➤ ❌  Delete product
                [3] ➤ 📋  Show products
                [4] ➤ 📄  Show all orders
                [5] ➤ 👥  Show all users
                [6] ➤ 🔓  Logout
        
        ==================================================
    """)
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        admin_views.add_product()
    elif choice == "2":
        admin_views.delete_product()
    elif choice == "3":
        user_views.show_products()
    elif choice == "4":
        admin_views.show_all_orders()
    elif choice == "5":
        views.show_all_users()
    elif choice == "6":
        views.logout()
    else:
        print("Invalid choice")
    return admin_menu()


def user_menu():
    print("""
        ==================================================
                                👤                       
                    🔷  U S E R   M E N U  🔷                      
                                👤                       
        ==================================================
        
                [1] ➤ 🛍️   Show all products
                [2] ➤ 🛒  Order product
                [3] ➤ 📦  My orders
                [4] ➤ 🔓  Logout
        
        ==================================================
    """)


    choice = input("Enter your choice: ")
    
    if choice == "1":
        user_views.show_products()
    elif choice == "2":
        user_views.order_product()
    elif choice == "3":
        user_views.show_my_orders()
    elif choice == "4":
        views.logout()
    else:
        print("Invalid choice")
    return user_menu()


if __name__ == "__main__":
    logout()
    auth_menu()
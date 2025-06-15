from core.file_manager import read


def show_all_orders():
    orders = read(filename="orders")
    if not orders:
        print("No orders yet")
        return

    for order in orders:
        print(f"ID: {order[0]} {order[1]}\t{order[2]}\t{order[3]}\t{order[4]}\t{order[5]}\t{order[6]}")

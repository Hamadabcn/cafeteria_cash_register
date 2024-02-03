products = {
    "Coffee": 2.50,
    "Tea": 1.75,
    "Sandwich": 5.00,
    "Salad": 4.50,
    "Soup": 3.25,
    "Soda": 1.50
}

def display_menu():
    print("\n---- Welcome to the Cafeteria! ----\n")
    print("\nProducts available: \n")
    for product, price in products.items():
        print(f"- {product}: ${price:.2f}")
    print("-------------------------------")

def calculate_total(order):
    total = 0
    for item in order:
        if item in products:
            total += products[item]
    return total

def process_order():
    order = []
    while True:
        product = input("Enter a product name (or 'q' to complete order): ")
        if product == "q":
            break
        elif product in products:
            order.append(product)
        else:
            print("Invalid product!")

    total = calculate_total(order)
    print(f"Total: ${total:.2f}")

display_menu()
process_order()

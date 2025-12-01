# Interactive program to calculate product price with 15% tax

# Product list with prices
products = {
    1: {"name": "Toyota Camry", "price": 24000},
    2: {"name": "BMW M4", "price": 55000},
    3: {"name": "Mercedes C-Class", "price": 40000},
    4: {"name": "Ford Mustang", "price": 30000},
    5: {"name": "Audi A4", "price": 35000}
}

TAX_RATE = 0.15  # 15% tax

def display_products():
    print("\n=== Product List ===")
    for number, info in products.items():
        print(f"{number}. {info['name']} - ${info['price']}")
    print("0. Leave")

def get_choice():
    try:
        choice = int(input("\nEnter the product number (or 0 to Leave): "))
        return choice
    except ValueError:
        print("Input must be a valid number!")
        return None

def calculate_price(price):
    return price * (1 + TAX_RATE)

# Main program loop
while True:
    display_products()
    choice = get_choice()
    
    if choice is None:
        continue  # Retry if invalid input
    
    if choice == 0:
        print("\nThank you for using the program! Goodbye.")
        break
    
    if choice in products:
        product = products[choice]
        total_price = calculate_price(product['price'])
        print(f"\nPrice of {product['name']} including 15% tax is: ${total_price:.2f}")
    else:
        print("The number you entered is not in the list! Please try again.")

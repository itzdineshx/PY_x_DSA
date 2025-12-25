# Concession Stand Menu for PVR Cinema

menu = {
    "Samosa": 15.00,
    "Egg Puffs": 20.00,
    "Corn": 50.50,
    "Lays": 15.00,
    "Pop Corn": 20.50,
    "Coco Cola": 25.00,
    "Tea": 12.00,
    "Coffee": 15.00
}

cart_item = [] # user cart items
total_price = 0 # initial ampount of order


# Greets the customer and displays the menu
print("----- Welcome to PVR Menu -----")
for item, price in menu.items():
    print(f"{item:10}: ₹{price:.2f}")
print("-------------------------------")


# Taking orders from the customer and adding to cart
while True:
    choice = input("Enter the item you want to order (or 'q' to quit): ").title()
    if choice.lower() == 'q':
        break
    if choice in menu:
        cart_item.append(choice)
        total_price += menu[choice]
        print(f"{choice} added to your cart. Current total: ₹{total_price:.2f}")
    else:
        print("Sorry, we don't have that item. Please choose from the menu.")


print("\n----- Your Order Summary -----").center(40)
for item in cart_item:
    print(f"- {item}: ₹{menu[item]:.2f}")
print(f"Total Amount Due: ₹{total_price:.2f}")
print("-------------------------------")
print("Thank you for ordering at PVR! Enjoy your movie!🍿🎬")
# Shopping Cart 
# Declaring Cart Variables
foods = []
prices = []
total = 0

while True:
    food = input("Enter food item (or 'q' to Quit): ").lower()
    if food == 'q':
        break
    food_price = float(input(f"Enter price for {food} in ₹: "))
    foods.append(food)
    prices.append(food_price)

# Display Cart Summary
print("\n--- Shopping Cart Summary ---")
for i in range(len(foods)):
    print(f"{foods[i].title()}: ₹{prices[i]:.2f}")
    total += prices[i]

print(f"Total Amount: ₹{total:.2f}")
print("--------------------")
print("Thank you for shopping with us!😘")

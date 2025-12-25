# arbitary arguments - *args, **kwargs

# Arbitrary Positional Arguments - *args
# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(add(1, 2, 3))  # Output: 6
# print(add(5, 10, 15, 20, 25))  # Output: 75

# # Arbitrary Keyword Arguments - **kwargs
# def display_info(**kwargs):
#     for key, val in kwargs.items():
#         print(f"{key}: {val}")

# display_info(name="Dinesh", age=20, city="Chennai")
# display_info(product="Laptop", price=1200, quantity=2)

def ship_order(order_id, *items, **details):
    print(f"Order ID: {order_id}")
    print("\nItems to be shipped:")
    for item in items:
        print(f"- {item}")
    print("\nShipping Details:")
    for key, val in details.items():
        print(f"{key}: {val}")

ship_order(101, "Laptop", "Mouse", "Keyboard", address="porur", city="Chennai", zip="600001")
#function call(default arg, arbitary positional arg, arbitary keyword arg)
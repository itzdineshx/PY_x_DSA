# This program generates a simple invoice for purchased items.

def display_invoice(username, amount, due_date):

    print("----------Invoice------------")
    print(f"Customer Name: {username:20}")
    print(f"Amount Due: ${amount:.2f}")
    print(f"Due Date: {due_date:20}")
    print("-----------------------------")
    print("Thank you for your business!")

display_invoice("Dinesh", 5000, "2025-07-15")
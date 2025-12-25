# Banking program

def show_balance(balance):
    print(f"Your current balance is: ₹{balance:.2f}")

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds.")
        return balance
    return balance - amount


def main():
    balance = 0.0
    is_running = True

    while is_running:
        print("\n-----------🙌 Welcome to IDBI Bank 🙌-----------")
        print("1. Show Balance, 2. Deposit, 3. Withdraw, 4. Exit")

        choice = input("\nChoose an option (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            amount = float(input("Enter amount to deposit: ₹"))
            balance = deposit(balance, amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: ₹"))
            balance = withdraw(balance, amount)
        elif choice == '4':
            is_running = False
        else:
            print("Invalid choice. Please try again.")

    print(f"Your final balance is: ₹{balance:.2f}")
    print("\n----------- 🙏 Thank You 🙏 -----------")

if __name__ == "__main__":
    main()
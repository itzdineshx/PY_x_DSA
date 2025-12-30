"""
CLI Slot Machine Game 🎰
"""
import random

# Constants
MAX_LINES = 3
MIN_BET = 10
MAX_BET = 10000
ROWS = 3
COLS = 3

# Emoji Symbols (Fixed)
symbol_count = {
    "😍": 2,
    "😎": 4,
    "🎂": 6,
    "🎁": 8
}

symbol_value = {
    "😍": 5,
    "😎": 4,
    "🎂": 3,
    "🎁": 2
}

# Spin the slot machine
def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

# Print the slot machine
def print_slot_machine(columns):
    print("\n🎰 Spinning...\n")
    for row in range(ROWS):
        for i, column in enumerate(columns):
            end = " | " if i < COLS - 1 else ""
            print(column[row], end=end)
        print()
    print()

# Check for wins
def check_win(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            win_amount = values[symbol] * bet
            winnings += win_amount
            winning_lines.append(line + 1)

    return winnings, winning_lines

# -------------------------------------------
# User Input Functions
# -------------------------------------------

def deposit():
    while True:
        amount = input("💰 How much would you like to deposit? ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
        print("❌ Invalid input. Please enter a positive number.")

def get_number_of_lines():
    while True:
        lines = input(f"🎯 Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
        print("❌ Invalid number of lines.")

def get_bet():
    while True:
        amount = input(f"🎲 Enter bet amount per line (₹{MIN_BET} - ₹{MAX_BET}): ₹")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
        print("❌ Invalid bet amount.")

# -------------------------------------------
# Play One Round
# -------------------------------------------

def play_game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"⚠️ You don't have enough balance (₹{balance}). Try again.")
        else:
            break

    print(f"✅ You bet ₹{bet} on {lines} lines. Total: ₹{total_bet}")
    slots = get_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_win(slots, lines, bet, symbol_value)

    print("🎉 Results:")
    print(f"💸 You won ₹{winnings}")
    if winning_lines:
        print(f"✅ Winning Lines: {', '.join(str(line) for line in winning_lines)}")
    else:
        print("😢 No winning lines this time.")

    return winnings - total_bet

# -------------------------------------------
# Main Loop
# -------------------------------------------

def main():
    balance = deposit()

    while True:
        print(f"\n💼 Current Balance: ₹{balance}")
        choice = input("▶️ Press Enter to spin or type 'q' to quit: ").lower()

        if choice == 'q':
            break

        balance += play_game(balance)

    print(f"\n🏁 Game Over! You left with ₹{balance}. Thanks for playing! 🎰")

# -------------------------------------------

if __name__ == "__main__":
    main()

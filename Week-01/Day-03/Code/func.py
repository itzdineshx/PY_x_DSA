# Functions (def()) - These are block of reusable code
import time

def new_year(name, year): # function declaration
    print("Starting the countdown...")
    for i in reversed(range(1,4)):
        time.sleep(1)
        print(i)
    print(f"Happy New Year {year} {name}!")
new_year("Dinesh", 2026) # function call

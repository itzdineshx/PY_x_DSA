"""
This is a Number Guessing game on the Command line Interface
"""
import random # for generate random numbers

# Fetch number for guess from user
top_range = input("Type a number for Guess: ")

# Check the input is digit
if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("please Type a number larger than 0 >.<")
        quit()
else:
    print("Type a Number Next Time :(")
    quit()

# generates Random Number
rand_num = random.randint(0,top_range)
guess = 0 # tracks guesses

while True:
    guess += 1
    user_guess = input("Make a Guess: ")

    # Check the user input is digit
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a Number Next Time :(")
        continue
    
    if user_guess == rand_num:
        print("you Gotcha :)")
        break
    elif user_guess > rand_num:
        print("you Were Above the Number")
    else:
        print("you Were Below the Number")

# final result
print(f"You made it in {guess} guesses")
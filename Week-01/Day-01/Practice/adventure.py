"""
This is a Adventure game Based on user input on the Command line Interface
"""
# user welcome
user_name = input("Enter Your name: ")
print(f"Welcome {user_name} to this adventure game!")

# story
print("\nYou came to an adventure on your own to find a treasure, which is marked on a map that you find under a tree.")
print("...")
print("So, You decide to go to there without informing anyone. After you reached it is a wild forest after some long travelling when you get rest unfortunately you were nearly attacked by a lion")
print("...")
print("you got scared and run then you were missed on that forest and your map got gone somewhere")
print("...")
print("\nNow, You are on a dirt road, it has come to an end and you can go left or right. ")

# option 1
answer = input("Which Way would you choose?(left/right): ").lower()

if answer == "left":
    print("\nYou Come to a River, You Can Walk Around it or Swim Accross")
    answer = input("How Can you go?(Walk/Swim): ").lower()

    if answer == "swim":
        print("You were Eaten by an aligator")
    elif answer == "walk":
        print("You walked for many miles and you are dead")
    else:
        print("not a Valid option")
        print("You Lose :(")

# option 2
elif answer == "right":
    print("\nYou Come to a Bridge, it looks wobbly and very old you can cross it or head back")
    answer = input("What Would you Do?(cross/back): ").lower()

    if answer == "back":
        print("You go back and lost again in the forest.")

    elif answer == "cross":
        print("You Crossed a bridge and met a stranger, You ask for help or not")
        answer = input("Would you Ask for Help?(Yes/no) ").lower()

        if answer == "yes":
            print("He is a police under covered and he rescued you")
            print("you Won >..<")
        elif answer == "no":
            print("You walked for many miles to get out and you are dead")
        else:
            print("not a Valid option")
            print("You Lose :(")

    else:
        print("not a Valid option")
        print("You Lose :(")

else:
    print("not a Valid option")
    print("You Lose :(")

print("Thanks for Trying my Game ", user_name, ":)")
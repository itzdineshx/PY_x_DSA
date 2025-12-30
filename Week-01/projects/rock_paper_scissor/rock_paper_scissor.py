# This program is a Rock, Paper, Scissor 👊✌️✋ game on the Command line Interface
"""
Rock crushes Scissors (Rock wins).
Scissors cuts Paper (Scissors wins).
Paper covers Rock (Paper wins). 

rock > scissor
scissor > paper
paper > rock
"""

import random
import os

print("Welcome to Rock, Paper, Scissor Game!🤜🤛")

choices = ["rock", "paper", "scissor"]
emojis = {"rock": "✊", "paper": "✋", "scissor": "✌️"}
player = None
computer = random.choice(choices)

player = input("Enter your choice (rock✊/paper✋/scissor✌️): ").lower().strip()
while True:
    if player not in choices:
        player = input("Enter your choice (rock✊/paper✋/scissor✌️): ").lower().strip()
    else:
        break

print(f"\nYou chose: {player}{emojis[player]}")
print(f"Computer chose: {computer}{emojis[computer]}\n")

if player == computer:
    print("It's a Tie!🤝")
elif (player == "rock" and computer == "scissor") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissor" and computer == "paper"):
    print("You Win! 🎉")
else:
    print("Computer Wins! 💻")

print("Thanks for playing the Rock, Paper, Scissor Game!😊\n")

# restart option
restart = input("Do you want to play again? (Y/N): ").strip().lower()
if restart == "y":
    # Re-run the script
    os.system('python ' + __file__)
else:
    print("Thanks for playing the Rock, Paper, Scissor Game!😊")
exit()


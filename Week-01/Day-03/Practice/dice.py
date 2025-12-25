# Dice Roller Simulator in python

import random

# Dice art representation
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

                                
dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

# Rolling the dice  
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# Display the Dice in Vertical Manner
# for die in dice:
#     for line in dice_art[die]:
#         print(line)
#     print()

# Display the Dice in Horizontal Manner
for line in range(5):
    for die in dice:
        print(dice_art[die][line], end="  ")
    print()

for die in dice:
    total += die

print(f"Total rolled value: {total}\n")
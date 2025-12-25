"""
This is a simple Tech quiz game on the Command line Interface
"""

# welcomes user
print("Welcome to the Computer Quiz Game!\n")

# Decide whether to continue or not
playing = input("Do You Want to Play?(yes or no): ").lower()

# if player not wants to play
if playing != 'yes':
    print("Better Luck Next Time :(")
    quit() # game ends

print("Let's Play the Game...") # game begins

# introducing rules to the user
rules = """ These are the Rules of the game:
1. Answer the questions without spelling mistakes.
2. If it is correct points ++ otherwise points -- for each question.
3. Finally you will get your score.
"""
print(rules)
# points for user correct answer
points = 0
q_count = 0

q_count += 1
print(f"Question no: {q_count}")
# Question 1
answer = input("Expand CPU: ").lower()
if answer == "central processing unit":
    print("correct")
    points += 1 # increment score
else:
    print("Incorrect")
    points -= 1 # decrement score

# Question 2
q_count += 1
print(f"Question no: {q_count}")
answer = input("Expand GPU: ").lower()
if answer == "graphics processing unit":
    print("correct")
    points += 1 # increment score
else:
    print("Incorrect")
    points -= 1 # decrement score

# Question 3
q_count += 1
print(f"Question no: {q_count}")
answer = input("Expand RAM: ").lower()
if answer == "random access memory":
    print("correct")
    points += 1 # increment score
else:
    print("Incorrect")
    points -= 1 # decrement score

# Question 4
q_count += 1
print(f"Question no: {q_count}")
answer = input("Expand PSU: ").lower()
if answer == "power supply unit":
    print("correct")
    points += 1 # increment score
else:
    print("Incorrect")
    points -= 1 # decrement score

# Question 5
q_count += 1
print(f"Question no: {q_count}")
answer = input("Expand ROM: ").lower()
if answer == "read only memory":
    print("correct")
    points += 1 # increment score
else:
    print("Incorrect")
    points -= 1 # decrement score

# Executes the result
print("\nResult:")
print(f"You Answered {str(q_count)} questions")
print(f"Your Final Score is {points}")
print(f"Your Accuracy is {((points/q_count)*100)}%")
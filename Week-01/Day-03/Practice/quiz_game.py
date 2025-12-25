# Python quiz game
user = input("Enter your name to start or q to quit: ")
if user.lower() == "q":
    print("Goodbye!🤧")
    exit()

else:
    print(f"Welcome to the Quiz Game! {user}")

# Quiz Questions
questions = ("1. What is the key word for function in Python? ",
             "2. Which data type is used to store text? ",
             "3. Which symbol is used for comments in Python? ",
             "4. What are the mutable data types here in Python? ",
             "5. Which keyword is used to create a class in Python? ")
# Quiz Options
options = (["a) def", "b) func", "c) function", "d) define"],
           ["a) int", "b) str", "c) float", "d) bool"],
           ["a) //", "b) <!--", "c) #", "d) /*"],
           ["a) list, tuple", "b) dict, list", "c) tuple, str", "d) str, int"],
           ["a) function", "b) class", "c) def", "d) create"])

# Correct Answers
answers = ["a", "b", "c", "b", "b"]
guess = []
score = 0
questions_number = 0

# Loop through each question and display them
for question in questions:
    print("---------------------------")
    print(question)
    for option in options[questions_number]:
        print(option)

    guess_input = input("Enter your answer (a/b/c/d): ").strip().lower()
    guess.append(guess_input)

    if guess[questions_number] == answers[questions_number]:
        score += 1
        print("Correct!😍")
    else:
        print("Wrong!😥")

    questions_number += 1

# Display Final Score 
print("---------------------------")
print("Quiz Completed!😘")
print(f"Your Guesses: {guess}")
print(f"Correct Answers: {answers}")
print(f"{user}, your final score is: {score} out of {len(questions)}")
percentage = (score / len(questions)) * 100
print(f"Your percentage is: {percentage:.2f}%")
print("Thanks for playing the Quiz Game!😊")
print("---------------------------")

# re start option
print("Do you want to play again? (Y/N): ")
restart = input().strip().lower()
if restart == "y":
    exec(open(__file__).read())
    print("Restarting the game...👾")
else:
    print("Goodbye!🤧")
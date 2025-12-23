#user input
name = input("Enter something: ")
print(name)

#user input for command line
choice = input("Enter [1] Start [2] Stop: ")

if choice == "1":
    print("System starting...")
elif choice == "2":
    print("System stopping...")
else:
    print("Invalid choice")

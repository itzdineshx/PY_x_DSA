# Multi threading - Performs multiple tasks concurrently

import threading
import time

# Single Threading - All process in a single thread(Linear Execution)
def program_code():
    time.sleep(4)
    print("I am writting a Program now👨‍💻")

def listen_music():
    time.sleep(3)
    print("I am Listening to a music now 🎼")

def get_msg():
    time.sleep(1)
    print("I got a Message 📥")

# Function Calls
# program_code()
# listen_music()
# get_msg()

# Multi Threading - Multitasking simultaneously 
chore_1 = threading.Thread(target=listen_music)
chore_1.start()

chore_2 = threading.Thread(target=get_msg) # Small exec time first 
chore_2.start()

chore_3 = threading.Thread(target=program_code) # large exec time last 
chore_3.start()

# Concurrent Functions
chore_1.join()
chore_2.join()
chore_3.join()

print("All the chores are Completed Successfully!")
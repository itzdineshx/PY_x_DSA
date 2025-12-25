import time

my_time = int(input("Enter the time for Break in sec: "))
print("Break starts now!")

# Calculate initial hours, minutes, seconds
initial_hours = int(my_time / 3600)
initial_minutes = int((my_time % 3600) // 60)
initial_seconds = my_time % 60

print(f"The Stream will resume in: {initial_hours:02} hrs: {initial_minutes:02} min: {initial_seconds:02} sec")

# Countdown
for x in range(my_time, 0, -1):
    hours = int(x / 3600)
    minutes = int((x % 3600) // 60)
    seconds = x % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's up!")
# Vibe Time 🎧
"""
This program plays vibe music until the break time ends.

Steps:
1. Get break end time from user
2. Initialize audio once
3. Keep checking time
4. Stop music when break ends
"""

import time
import datetime
import pygame


def set_break_time(break_time_str):
    sound_file = "E:/projects/my_projects/Relearn_from_scratch/alarm/8bit_arcade.mp3"

    now = datetime.datetime.now()
    break_time = datetime.datetime.strptime(break_time_str, "%H:%M:%S").time()
    break_datetime = datetime.datetime.combine(now.date(), break_time)

    # If break time already passed today, assume next day
    if break_datetime <= now:
        break_datetime += datetime.timedelta(days=1)

    print(f"Break ends at: {break_datetime}")

    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)

    print("🎶 Vibe started...")

    while datetime.datetime.now() < break_datetime:
        print(
            f"Current time: {datetime.datetime.now().strftime('%H:%M:%S')}",
            end="\n"
        )
        time.sleep(1)

    pygame.mixer.music.stop()
    print("\n⏰ Break time ended. Music stopped.")


# Driver Code
if __name__ == "__main__":
    break_time = input("Enter the Break Time (HH:MM:SS): ")
    set_break_time(break_time)

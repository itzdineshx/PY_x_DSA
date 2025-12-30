import curses
from curses import wrapper
import time
import random

# Countdown timer before test begins
def countdown(stdscr, seconds=3):
    for i in range(seconds, 0, -1):
        stdscr.clear()
        stdscr.addstr(0, 0, f"Starting in {i}...")
        stdscr.refresh()
        time.sleep(1)

# Start screen
def start_test(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test :)")
    stdscr.addstr("\nPress any key to begin the countdown!")
    stdscr.refresh()
    stdscr.getkey()

# Display text with color coding, WPM, accuracy, time
def display_text(stdscr, target, current, wpm=0, accuracy=0, elapsed=0):
    stdscr.addstr(0, 0, target)
    stdscr.addstr(1, 0, f"WPM: {wpm}   Accuracy: {accuracy:.2f}%   Time: {int(elapsed)}s")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1) if char == correct_char else curses.color_pair(2)
        stdscr.addstr(2, i, char, color)

# Load random text
def load_text():
    try:
        with open("text.txt", "r") as f:
            lines = f.readlines()
            return random.choice(lines).strip()
    except FileNotFoundError:
        return "No text file found. Please create a file named 'text.txt' with sample sentences."

# Calculate accuracy
def calculate_accuracy(target, current):
    correct = 0
    for i in range(len(current)):
        if i < len(target) and current[i] == target[i]:
            correct += 1
    total = len(current) if current else 1
    return (correct / total) * 100

# Typing test logic
def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        stdscr.clear()
        elapsed = time.time() - start_time
        if elapsed == 0:
            elapsed = 1

        wpm = round((len(current_text) / (elapsed / 60)) / 5)
        accuracy = calculate_accuracy(target_text, current_text)

        display_text(stdscr, target_text, current_text, wpm, accuracy, elapsed)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if current_text:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

    return wpm, accuracy, elapsed

# Final result screen
def show_results(stdscr, wpm, accuracy, time_taken):
    stdscr.clear()
    stdscr.addstr(0, 0, "✅ Test Completed!\n")
    stdscr.addstr(1, 0, f"🕒 Time Taken: {int(time_taken)} seconds")
    stdscr.addstr(2, 0, f"⌨️  WPM: {wpm}")
    stdscr.addstr(3, 0, f"🎯 Accuracy: {accuracy:.2f}%")
    stdscr.addstr(5, 0, "Press any key to continue or ESC to exit...")
    stdscr.refresh()
    key = stdscr.getkey()
    return ord(key) != 27  # return False if ESC is pressed

# Main function
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Correct
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Incorrect
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Neutral

    while True:
        start_test(stdscr)
        countdown(stdscr)
        wpm, accuracy, time_taken = wpm_test(stdscr)
        cont = show_results(stdscr, wpm, accuracy, time_taken)
        if not cont:
            break

wrapper(main)

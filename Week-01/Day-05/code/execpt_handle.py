# Exceptional - An event that interrupts the flow of execution
# Exceptional Handling - We have to detect and prevent the error rate
# Popular errors - TypeError, ValueError, SyntaxError, IndendationError, KeyError, IndexError

# Try - Except - Finally
# Handling ZeroDivisionError

try:
    num = int(input("Enter a Numaber for divion: "))
    print(1/num)

except ZeroDivisionError:
    print("Yo M@ you cant divide by zero!")

except ValueError:
    print("You Idiot only enter the numbers")

except Exception:
    print("You made something dumb")

finally:
    print("Clean this shit@")


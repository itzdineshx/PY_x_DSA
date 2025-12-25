# return in functions
# return allows a function to send back a value to the caller 

# def add(a, b):
#     result = a + b
#     return result # it makes send to the caller the value of result

# print(add(3, 5))  # Output: 8


def greet_user(first_name, last_name):
    first_name = first_name.title()
    last_name = last_name.title()
    return f"Hello, {first_name} {last_name}, Welcome to the Stream!"  # returning a formatted string

message = greet_user("dinesh", "sridhar")
print(message)  # Output: Hello, Dinesh Kumar!
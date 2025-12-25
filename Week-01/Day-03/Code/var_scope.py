# Variable Scope - Where a variable can be accessed in the code
# Scope Rule - LEGB: Local, Enclosing, Global, Built-in

x = 100  # Global scope
def outer_function():
    a = 10  # Enclosing scope
    print(x)  # Accessing global variable
    print(a)  # Accessing enclosing variable
    def inner_function():
        b = 5  # Local scope- initialized within a function
        print(x)  # Accessing global variable
        print(a)  # Accessing enclosing variable
        print(b)  # Accessing local variable
    inner_function()
outer_function()
print(x)  # Accessing global variable
# print(a)  # Error: 'a' is not defined in global scope
# print(b)  # Error: 'b' is not defined in global scope
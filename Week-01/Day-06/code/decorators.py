# Decorators - functions that extends the behaviour of another functions
# It performs without modifying the base function only pass base func as arg

# Decorator Function with wrappers
def add_corn(func): # only executes when we calls the func
    def wrapper(*args, **kwargs): # accepts any parameters as inputs
        print("You added Corn 🌽")
        func(*args, **kwargs)
    return wrapper

@add_corn # Decorator trigger to execute
def get_soup(flavour):
    print(f"Here is your {flavour} soup 🍲...")

get_soup("Pepper")
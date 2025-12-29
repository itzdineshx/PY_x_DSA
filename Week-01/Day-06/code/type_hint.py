# Type Hints - allow developers to annotate their code with expected types for variables and function arguments
age: int = 25
def greet(name: str) -> str:
    return f"Hello, {name}!"
print(greet("Subscribers"))

def add_numbers(x: int, y: int) -> int:
    return x + y
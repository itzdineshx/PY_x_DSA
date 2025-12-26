# super() function is used to call methods from a parent (superclass) inside a child (subclass)
# Works with single, multiple, and multilevel inheritance.
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.radius = width

class Triangle(Shape):
    def __init__(self, color, filled, height):
        super().__init__(color, filled)
        self.radius = height

circle_1 = Circle("red", True, 4)
print(f"{circle_1.color}")

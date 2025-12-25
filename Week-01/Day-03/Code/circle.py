# Circle Module
import math

def area(radius):
    return math.pi * radius ** 2
def circumference(radius):
    return 2 * math.pi * radius
def diameter(radius):
    return 2 * radius

# Example usage:
if __name__ == "__main__":
    r = 5
    print(f"Area of circle with radius {r}: {area(r)}")
    print(f"Circumference of circle with radius {r}: {circumference(r)}")
    print(f"Diameter of circle with radius {r}: {diameter(r)}")

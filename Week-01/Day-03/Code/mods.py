# modules - a file containing Python code (functions, variables, etc.) that can be imported and used in other Python files

import circle
r = int(input("Enter the radius of the circle: "))
print(f"Area of circle with radius {r}: {circle.area(r)}")
print(f"Circumference of circle with radius {r}: {circle.circumference(r)}")
print(f"Diameter of circle with radius {r}: {circle.diameter(r)}")
# PooP - Python Object Oriented Programming
# Objects - it's a bundle of attributes(var) and methods(fn)
# Class - collection of objects and design the structure and layout of object(blueprint)

from car import Car # Importing the Car Module

car1 = Car("Audi R8", "Red", 2020, True) # creating an obj of class car

print(f"I love to ride the {car1.model} of {car1.year} edition, especially the {car1.color} one.") # returning the car1 obj
print(f"Is the car for sale? {car1.for_sale}")

car1.drive() # calling the drive method from the Car Module
print(f"Yo Bro i have a {car1.describe()}")
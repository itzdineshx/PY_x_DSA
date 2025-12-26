# Inheritance - Allows a class to inherit the attributes and methods from another class.
# Inheritance allows a class (child class) to acquire properties and methods of another class (parent class).
# It make better re-usablility, encapsulation , extensibility
"""
Types of Inheritance:
1. Single Inheritance: A child class inherits from a single parent class.
2. Multiple Inheritance: A child class inherits from more than one parent class.
3. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
5. Hybrid Inheritance: A combination of two or more types of inheritance.
"""

class Animal:
    origin = "Earth"

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        return f"{self.name} is eating."

    def type(self):
        return f"{self.name} is a {self.species} from the {Animal.origin}."

class Dog(Animal):
    def speak(self):
        return("wol... wol...!")

class Cat(Animal):
    def speak(self):
        return("meow... meow...!")

class Lion(Animal):
    def speak(self):
        return("Raar... wraar...!")

dog1 = Dog("Tommy", "Dog")
cat1 = Cat("Karuppu", "Cat")
lion1 = Lion("leo", "Lion")

print(f"MY Dog name is {dog1.name} and {dog1.eat()} with my cat {cat1.name}")
print(f"My lion {lion1.name} will make a sound of {lion1.speak()}")
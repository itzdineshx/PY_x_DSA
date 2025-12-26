# Multiple Inheritance - A child class inherits from more than one parent class.
# Multi-level Inheritance - A child class inherits from a parent class, which in turn inherits from another class.

# Main class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"This {self.name} is eating!"

    def eat(self):
        return f"This {self.name} is eating!"
    
# Single Inheritance: C(X)
class Prey(Animal):
    def flee(self):
        return f"This {self.name} is fleeing"

class Predator(Animal):
    def hunt(self):
        return f"This {self.name} is hunting"


# Multi-level Inheritance: C(A) <- B(A) <- A(B)
class Rabbit(Prey):
    pass

class Tiger(Predator):
    pass

# Multiple Inheritance: C(A,B)
class Fish(Prey, Predator): 
    pass


rabbit1 = Rabbit("Vindhu")
tiger1 = Tiger("veera")
fish = Fish("meenu")

print(tiger1.hunt())
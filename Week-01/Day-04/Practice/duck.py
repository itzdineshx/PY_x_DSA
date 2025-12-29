# Polymorphism - means "many forms"  to perform different actions based on the context.
"""
2. Duck Typing - object must have the minimum necessary attribute
Duck-typing emphasis what the object can really do, rather than what the object is.
"""
class Bird:
    def fly(self):
        print("fly with wings")

class Airplane:
    def fly(self):
        print("fly with fuel")

class Fish:
    def swim(self):
        print("fish swim in sea")

# Attributes having same name are
# considered as duck typing
for obj in Bird(), Airplane(), Fish():
    obj.fly()
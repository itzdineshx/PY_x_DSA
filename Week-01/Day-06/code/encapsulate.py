# Encapsulation  - hiding internal details of a class and only exposing what’s necessary
class Person:
    def __init__(self, name, age, gender):
        self.__name = name # private attribute
        self._age = age # protected attribute
        self.gender = gender # public attribute

    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, value):
        self.__name = value

p1 = Person("Dinesh", 20, 'm')
print(p1.Name)
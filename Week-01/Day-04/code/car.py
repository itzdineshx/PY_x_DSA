"""This module defines a class car with various attribute of car"""
class Car:
    def __init__(self, model, color, year, for_sale): # thunder method
        # Pre defined attributes
        self.model = model # model of a car
        self.color = color # color of a car
        self.year = year # year of manufacture
        self.for_sale = for_sale # is it sale or not?

    # Methods of the class Car
    def drive(self):
        return(f"You are driving the world famous {self.model} car with color of {self.color} 🚗")

    def stop(self):
        return(f"You have stopped the {self.model} car🛑")

    def describe(self):
        return(f"The car model is {self.model} with color {self.color} manufactured in the year {self.year} and it is {self.for_sale} now.")

# Static Method - A method that belongs to a class rather than any object from that class

class Employee:

    def __init__(self, name, position):
        self.name= name
        self.position = position

    # Instance Method
    def get_stat(self):
        return f"{self.name} is {self.position}"
    
    # Static method
    @staticmethod
    def is_val_position(position):
        valid_position = ["Designer", "Developer", "Tester"]
        return position in valid_position

emp1 = Employee("Dinesh", "Developer")
emp2 = Employee("Naveen", "Cook")

print(Employee.is_val_position("Developer")) # Static Method
print(emp1.get_stat()) # Instance Method
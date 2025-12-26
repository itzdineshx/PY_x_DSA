# Class Method - Allow Operations related to the class itself

"""
Note:
1. Instance Methods - Best for operations on instance of class(objects)
2. Static Methods - Best for utility functions that do not need acess to class data(nethods)
3. Class Methods - Best for Class Level data or require acess to the class itself(class)
"""


class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance Method - Acessed by Objects
    def get_stat(self):
        return f"{self.name} {self.gpa}"

    # Class Method - Acessed by class Attributes
    @classmethod
    def get_cnt(cls):
        return f"Total No of Students: {cls.count}"

    @classmethod
    def avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"

stud_1 = Student("Dinesh", 8.5)
stud_2 = Student("Naveen", 9.7)

print(f"There are {Student.get_cnt()} Students")
print(f"The Average GPA {Student.avg_gpa()}")
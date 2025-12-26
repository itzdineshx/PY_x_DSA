# Class Variable - shared across all instances of a class.
# Instanve Varible - unique to each instance

class Student:
    college_name = "DMI College of Engineering" # Class Varible - can be call by the class name itself
    num_students = 0

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Dinesh", 20)
student2 = Student("Naveen", 21)

print(f"{student1.name} is Studying in {Student.college_name} and his age is {student1.age}")
print(f"The Number of students Studying in the {Student.college_name} is {Student.num_students}")
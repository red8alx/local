#Exercise 1: Creating a Student Class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_student_information(self):
        full_information = f"Student Information:\nName: {self.name}\nAge: {self.age}"
        print(full_information)
my_student = Student("Rediet", 38)
my_student.get_student_information()


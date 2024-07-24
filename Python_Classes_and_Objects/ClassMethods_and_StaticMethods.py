#Class Methods
"""class Student:
    count = 0 # Class variable to count instances
    
    def __init__(self, name):
        self.name = name
        Student.count += 1 # Increment count on instance creation
    @classmethod #Indicate the method belongs to the class
    def display_count(cls):
        print(f"Total students object created: {cls.count}")
my_student1 = Student("Bob")
my_student2 = Student("Alice")
Student.display_count()
print(f"Total students object created: {Student.count}")"""
#Static Methods
class MathUtils:
    @staticmethod
    def add(x, y): #Function declaration does not require the parameters "self" or "cls"
        return x + y
    @staticmethod
    def multiply(x, y):
        return x * y
#However the static methods still have to be called with the class reference
print(MathUtils.add(5, 3))
print(MathUtils.multiply(5, 3))
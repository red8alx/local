#Exercise 1: Class Methods for Counting Instances Instruction:
"""class Book:
    count = 0
    def __init__(self,title):
        self.title = title
        Book.count +=1
    @classmethod
    def display_total_books(cls):
        print(f"Total books created: {cls.count}")
my_book1 = Book("C++ Illustrated")
my_book2 = Book("Python for Beginners")
Book.display_total_books()"""

#Exercise 2: Static Method for Utility Calculation Instruction:
"""class Calculator:
    @staticmethod
    def addition(a, b):
        return a + b
    @staticmethod
    def multiplication(a, b):
        return a * b
print(Calculator.addition(2, 9))
print(Calculator.multiplication(2, 9))"""

#Exercise 3: Class Method for Factory Creation Instruction:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def create_child(cls, name, age):
        cls.name = name
        cls.age = age
        Person(cls.name, cls.age)
Person.create_child("Bob", 0)
#Exercise 1: Constructors and Destructors Instructions:
"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def personal_info(self):
        print(f"Personal Information:\nName: {self.name}\nAge: {self.age}")
    def __del__(self):
        print("Object destructored...")
my_person = Person("Bob", 26)
my_person.personal_info()"""

#Exercise 2: Magic Methods (str and repr) Instructions:
"""class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"\"{self.title}\" by {self.author} with {self.pages} pages"
my_book = Book("Introduction to Python", "John Doe.", 345)
print(my_book)"""

#Exercise 3: Class Inheritance Instructions:
class Animal:
    def eat(self):
        print("Animal eating...")
    def sleep(self):
        print("Animal sleeping...")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
my_animal = Animal()
my_dog = Dog()
my_dog.eat()
my_dog.sleep()
my_dog.bark()
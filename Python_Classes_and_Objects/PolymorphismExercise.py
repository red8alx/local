#Exercise 1: Single Inheritance Instruction:
"""class Shape:
    def calculate_area(self):
        print("Calculating the area of a Shape...")
class Rectangle(Shape):
    def calculate_area(self):
        print("Calculating the area of a Rectangle...")
my_rectangle = Rectangle()
my_rectangle.calculate_area()"""

#Exercise 2: Multiple Inheritance Instruction:
"""class Bird:
    def fly(self):
        print("Flying as a bird...")
class Mammal:
    def run(self):
        print("Running as a mammal...")
class Bat(Bird, Mammal):
    pass
my_bat = Bat()
my_bat.fly()
my_bat.run()"""

#Exercise 3: Polymorphism with Duck Typing Instruction:
class Dog:
    def make_sound(self):
        print("Dog making sound...")
class Cat:
    def make_sound(self):
        print("Cat making sound...")
class Bird:
    def make_sound(self):
        print("Bird making sound...")
def let_them_speak(obj):
    obj.make_sound()

my_dog = Dog()
my_cat = Cat()
my_bird = Bird()

let_them_speak(my_dog)
let_them_speak(my_cat)
let_them_speak(my_bird)

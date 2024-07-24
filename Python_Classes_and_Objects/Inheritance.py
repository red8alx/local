class Animal:
    def __init__(self,name):
        self.name = name
    def message(self):
        print("I am an animal!!")
    def make_sound(self):
        print("Generic animal sound")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def make_sound(self):
        print("Woof!!!")

my_dog = Dog("Bobby", "Pitbull")
my_dog.message()
my_dog.make_sound()


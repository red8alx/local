class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Personal Infomation:\nName: {self.name}\nAge: {self.age}" #This method should return a string as it is the string representation of the object
    def __repr__(self):
        strRep = "string represntation"
        #Find out what this method does and how it differs from the __str__() method
my_person = Person("Abebe", 20)
print(my_person)
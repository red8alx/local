#Exercise 1: Write a function to greet the user by name.
def greeting(name):
    print(f"Welcome Mr. {name}" )
greeting("Rediet")
#Exercise 2: Create a function to calculate the area of a rectangle.
def areaOfTriangle(height, width):
    area = (height * width) / 2
    return area
area = areaOfTriangle(height = 10, width = 20)
print(f"The area of the triangle is: {area}")
#Exercise 3: Develop a function to check if a number is even or odd.
def checkEvenOrOdd(number):
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")
checkEvenOrOdd(2)
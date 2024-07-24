#Exercise 1: Handling ZeroDivisionError
"""def division():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Exception Occured. /0")
    else:
        print(f"Division result: {result}")
division()"""
#Exercise 2: File Handling with FileNotFoundError
"""try:
    raise FileNotFoundError()
except FileNotFoundError as e:
    print(e)
print("File not found Exception handled.")"""
#Exercise 3: Custom Exception
class ValueTooHighError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"{self.value} is too high. Exception occured."
def value_checker(value):
    try:
        if value > 100:
            raise ValueTooHighError(value)
    except ValueTooHighError as e:
        print(e)
    else:
        print(f"{value} is acceptable")
user_input = int(input("Enter a value: "))
value_checker(user_input)
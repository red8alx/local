number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
print("Enter one of the following operation:")
operation = input("Type 'A' for addition\nType 'S' Subtraction\nType 'M' for Multiplicatioj\nType 'D' for Division\n")
if (operation == 'A'):
    print(number_1 + number_2)
elif(operation == 'S'):
    print(number_1 - number_2)
elif(operation == 'M'):
    print(number_1 * number_2)
elif(operation == 'D'):
    print(number_1 / number_2)
else:
    print("Wrong Input")






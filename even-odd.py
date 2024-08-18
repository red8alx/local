number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
product = number_1 * number_2

if (product % 2 == 0):
    sum = number_1 + number_2
    print(f"The sum of {number_1} and {number_2} is {sum}")
else:
    difference = number_1 - number_2
    print(f"The difference of {number_1} and {number_2} is {difference}")

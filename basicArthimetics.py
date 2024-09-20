def display_menu():
    print("select you operation:")
    print("Type 1. For Addition")
    print("Type 2. For Subtraction")
    print("Type 3. For Multiplication")
    print("Type 4. For Division")
    print("Type 5. For Exiting the operation")
def sum(x,y):
    return x + y
def sub(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def operator():
    while True:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        display_menu()
        choice = int(input("Enter your choice: "))

        if(choice == 1):
            result = sum(a,b)
            print(f"The sum of the two numbers is : {result}")
        elif(choice == 2):
            result = sub(a,b)
            print(f"The differece of the two numbers is : {result}")
        elif(choice == 3):
            result = multiply(a,b)
            print(f"The product of the two numbers is : {result}")
        elif(choice == 4):
            result = divide(a,b)
            print(f"The division of the two numbers is : {result}")
        elif(choice == 5):
            print("Exiting..., Good bye!")
            break
        else:
            print("Invalid choice. Please try again.")
operator()
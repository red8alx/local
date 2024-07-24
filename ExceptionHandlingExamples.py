def divide(x,y):
    try:
        result = x/y
        raise ZeroDivisionError()
    except ZeroDivisionError:
        print("Division by Zero Error occured")
    else:
        print(f"Division Result: {result}")
    finally:
        print("Inside Finally Clause")
divide(10,0)
print("After divide() function call")
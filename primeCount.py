n1 = int(input("Enter a first number: "))
n2 = int(input("Enter a second number: "))
while (n1 < (n2-1)):
    n = n1 + 1
    i = 2
    isprime = True
    while((i <= n//2) and isprime):
        if(n % i == 0):
            isprime = False
        i = i + 1
    if (isprime):
        print(f"{n} is a prime number.")
    n1 = n1 + 1
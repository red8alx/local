n = int(input("Enter a number: "))
i = 2
isprime = True
while((i <= n//2) and isprime):
    if(n % i == 0):
        isprime = False
    i = i + 1
if (isprime):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is NOT a prime number.")
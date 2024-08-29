n = int(input("Enter a number: "))
sum = 0
i = 0
while (i < n):
    if(i % 2 == 0):
        sum += i
    i = i + 1
print(f"The sum is {sum}")
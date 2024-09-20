num = int(input("Enter a number: "))
copyNum = num
sum = 0
while(num > 0):
    digit = num % 10
    num = num // 10
    #print(digit, end="")
    if(digit % 2 ==0):
        sum += digit
print(f"The sum of the digits that are even in the number {copyNum} is {sum}")

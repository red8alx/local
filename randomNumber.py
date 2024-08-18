import random
secret_number = random.randint(1,100)
#print(secret_number)
guess_number = int(input("I have generated a random number b/n 1 - 100, Enter your guess \n"))
if (secret_number ==guess_number):
    print("Congrats, you found it")
elif (secret_number > guess_number):
    print("Wrong. Your guess was smaller than the random number, try bigger!")
else:
    print("Sorry. Your guess was bigger than the random number, try smaller!")

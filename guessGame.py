import random

secret_number = random.randint(1,100)
guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it?"))
guess_count = 0

print("Secret number:" , secret_number)
print("Guess:", guess)

match secret_number:
    case secret_number if secret_number == guess:
        print("Congratulations, you guessed it!")
    case secret_number if secret_number > guess:
        print("Nope, your guess is a bit low. Try bigger!")
    case secret_number if secret_number < guess:
        print("Oops, your guess is a bit high. Try smaller!")
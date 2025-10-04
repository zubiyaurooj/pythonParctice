import random

print("Welcome to the number Guessing game!")
print("i'm thinking of a number between 1 and 100...")

secret_number = random.randint(1,100)
attempts=0
guess = 0

while guess!= secret_number:
    guess=int(input("Enter your guess: "))
    attempts += 1

    if guess< secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} tries.")
import random  # We use the random module to generate random numbers.

print("🎲 Welcome to the Number Guessing Game 🎲")
print("I have chosen a number between 1 and 50. Can you guess it?")

# Step 1: Generate a random number between 1 and 50.
secret_number = random.randint(1, 50)
# secret_number holds the random number. We don’t show it to the user.

attempts = 0  # This variable will count how many guesses the player made.

# Step 2: Keep asking until the player guesses correctly.
while True:  # This loop runs again and again until we break it.
    guess = int(input("Enter your guess: "))  # Take input from the user.
    attempts += 1  # Add 1 to attempts each time.

    # Step 3: Compare the guess with the secret number.
    if guess < secret_number:  
        print("Too low! Try again.")  # Player guessed a smaller number.
    elif guess > secret_number:  
        print("Too high! Try again.")  # Player guessed a bigger number.
    else:  
        # This runs if guess == secret_number.
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        break  # Break stops the loop once correct guess is made.

import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "🎉 You win!"
    else:
        return "😞 You lose!"

def play_game():
    print("🎮 Rock, Paper, Scissors Game!")
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(get_winner(user_choice, computer_choice))

# Run the game
play_game()
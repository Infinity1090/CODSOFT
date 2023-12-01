# Rock-Paper-Scissors Game In Python.

import random
def get_user_choice():
    while True:
        print("\nRock, Paper, or Scissors?")
        user_choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"
def main():
    user_wins = 0
    computer_wins = 0
    ties = 0
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_wins += 1
        elif result == "Computer wins!":
            computer_wins += 1
        else:
            ties += 1
        print(f"User wins: {user_wins}, Computer wins: {computer_wins}, Ties: {ties}")
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break
    print("Thanks for playing Rock, Paper, Scissors!")
main()

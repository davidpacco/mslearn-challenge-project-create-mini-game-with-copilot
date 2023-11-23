# make a rock, paper, scissors game. After every round ask the user if they want to play again. Keep playing until the user doesn't want to play anymore. IF the user choose not to play, print out how many times they won, lost, and tied.
# 1. Ask the user for their choice (rock, paper, scissors)
# 2. Randomly generate the computer's choice
# 3. Determine who won
# 4. Ask the user if they want to play again
# 5. Keep track of wins, losses, and ties
# 6. Print out the wins, losses, and ties at the end

import random

def main():
    wins = 0
    losses = 0
    ties = 0
    play_again = True

    while play_again:
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("Computer chose: ", computer_choice)

        if user_choice == computer_choice:
            print("You tied!")
            ties += 1
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You won!")
            wins += 1
        elif user_choice == "paper" and computer_choice == "rock":
            print("You won!")
            wins += 1
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You won!")
            wins += 1
        else:
            print("You lost!")
            losses += 1

        play_again = input("Do you want to play again? (y/n): ") == "y"

    print("You won ", wins, " times.")
    print("You lost ", losses, " times.")
    print("You tied ", ties, " times.")

main()
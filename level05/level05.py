import math
import random

print("Welcome to Rock, Paper, Scissors!")

game_rounds = -1

# safely get round count from player
while game_rounds == -1:
    requested_rounds = input("How many rounds would you like to play? ")

    # handle general bad input
    try:
        requested_rounds = int(requested_rounds)
    except:
        print("Invalid input. Please enter an odd integer.")
        continue

    # use mod operator to easily determine even/odd (remainder of 0 means even, 1 would mean odd)
    if requested_rounds % 2 == 0:
        print("Invalid input. The number of rounds must be odd.")
        continue

    game_rounds = requested_rounds

valid_choices = ["rock", "paper", "scissors"]

# Prompts the user to enter a choice. Guaranteed returns a valid option from valid_choices.
def get_player_choice() -> str:
    # while true is technically a cardinal sin, but this is trivial enough it's realistically fine
    while True:
        player_input = input("Enter 'rock', 'paper', or 'scissors': ")
        if player_input in valid_choices:
            return player_input
        else:
            print(f"Sorry, '{player_input}' is not a valid choice. Try again.")

# Given the player's choice and the computer's choice, returns who won.
# Returns "tie" if both choices are identical.
# Returns "player" if the player's choice beats the computer's
# Returns "computer" if the computer's choice beats the player's
def determine_winner(player_choice: str, computer_choice: str) -> str:
    if player_choice == computer_choice:
        return "tie"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "player"
    else:
        return "computer"

played_rounds = 0
player_wins = 0

print(" ")

# Actual game loop
# Gets player/computer choices, determines winner, and loops until there is a winner
while played_rounds < game_rounds:
    player_choice_input = get_player_choice()
    computer_choice_rand = random.choice(valid_choices)
    winner = determine_winner(player_choice_input, computer_choice_rand)

    print(f"The computer chose {computer_choice_rand}.")

    if winner == "player":
        print("You won!")
        played_rounds += 1
        player_wins += 1
    elif winner == "computer":
        print("You lost!")
        played_rounds += 1
    else:
        print("Tie! Play again.")

    print(" ")

# Print final game results
print("========== GAME RESULTS ==========")
print(f"Score -- YOU: {player_wins} | COMPUTER: {played_rounds - player_wins}")
if player_wins >= math.ceil(played_rounds / 2):
    print("You win! Congrats!")
else:
    print("The computer won this time, but you can try again!")
print("Thanks for playing!")

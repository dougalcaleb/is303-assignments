import random
from level0607.words import wordlist

def choose_word() -> str:
    return random.choice(wordlist)

def get_guess() -> str:
    user_input_valid = False
    user_input = ""

    # loop until we get a valid user input
    while not user_input_valid:
        user_input = input("Enter a five-letter word: ").strip().lower()

        if len(user_input) != 5: # guard against long/short inputs
            print("The word must be exactly 5 letters long.")
        elif not user_input.isalpha(): # guard against inputs that contain chars other than letters
            print("The word must only contain letters.")
        else:
            user_input_valid = True

    return user_input

def evaluate_guess(guess: str, answer: str) -> str:
    evaluation = ["", "", "", "", ""]
    unclaimed_letters = list(answer)

    # Process greens first, since if we try to do yellows at the same time, it may claim a letter
    # we have not yet reached. There's probably some smarter logic that could reduce this to one loop,
    # but this works fine and is simple.
    for i in range(len(answer)):
        if guess[i] == answer[i]:
            evaluation[i] = "G"
            unclaimed_letters.remove(answer[i])

    # Process yellows/wrong letters
    for i in range(len(answer)):
        if evaluation[i] == "G":
            continue
        if guess[i] in unclaimed_letters:
            evaluation[i] = "Y"
            unclaimed_letters.remove(guess[i])
        elif evaluation[i] == "":
            evaluation[i] = "-"

    return " ".join(evaluation)

def display_guess(guess: str, feedback: str) -> None:
    guess_with_spaces = " ".join(list(guess))
    print(guess_with_spaces)
    print(feedback)

def has_won(feedback: str) -> bool:
    # We'll just determine correctness by analyzing the feedback, and if there's no yellows or dashes,
    # then there must only be greens, which means they got it correct.
    if "Y" not in feedback and "-" not in feedback:
        return True
    return False












# I know this wasn't part of the spec, but it makes testing it so much easier
def display_letters_remaining(guesses: list[str]) -> None:
    keyboard_layout = [
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
        [" ", "Z", "X", "C", "V", "B", "N", "M"]
    ]

    # create flat set of all letters used
    letters_in_words = [list(guess) for guess in guesses]
    letters_used = set([l.upper() for word in letters_in_words for l in word])

    for keyboard_row in keyboard_layout:
        row_output = ""
        for keyboard_letter in keyboard_row:
            if keyboard_letter in letters_used:
                row_output += keyboard_letter.lower()
            else:
                row_output += keyboard_letter.upper()
            row_output += " "

        print(row_output)
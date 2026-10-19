from level0607.wordle_functions import choose_word, get_guess, evaluate_guess, display_guess, has_won, display_letters_remaining

playing = True

# program loop, only quits when the user ctrl-c's or answers no when asked to play again
while playing:
    print("Welcome to Legally Distinct Wordle!")
    print("Guess the five-letter word.")
    print(" ")
    print("=== Legend: ==========================")
    print("G = correct letter and position")
    print("Y = correct letter, incorrect position")
    print("- = letter is not in the word")
    print("======================================")

    max_attempts = 6
    attempts_taken = 0
    user_guesses = []

    correct_answer = choose_word()

    # single game loop
    while attempts_taken < max_attempts:
        attempts_taken += 1

        print(" ")
        print(f"Attempt {attempts_taken} of {max_attempts}")
        user_guess = get_guess()

        if user_guess in user_guesses:
            print(f"You have already guessed '{user_guess}'. Try something else.")
            attempts_taken -= 1
            continue

        user_guesses.append(user_guess)

        user_guess_evaluation = evaluate_guess(user_guess, correct_answer)

        display_guess(user_guess, user_guess_evaluation)
        display_letters_remaining(user_guesses)

        if has_won(user_guess_evaluation):
            print(" ")
            print(f"Nice job! You got it in {attempts_taken} guesses.")
            break # using break for simpler while condition
        elif attempts_taken == max_attempts:
            print(" ")
            print(f"You didn't get it this time. The word was '{correct_answer}'.")
            # no break, will exit naturally

    play_again = input("Would you like to play again? [Y/n] ")
    if not (play_again.lower() == "y" or play_again.lower() == "yes" or len(play_again) == 0):
        print("Thanks for playing!")
        playing = False


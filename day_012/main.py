# Number Guessing Game

import random
from art import logo


def new_hidden_number():
    return random.randint(1, 100)


def guess_result(hidden, guess):
    is_guessed = False
    if guess > hidden:
        print("Too high. Try again!")
    elif guess < hidden:
        print("Too low. Сome on again!")
    else:
        is_guessed = True
        print("Wow! You did it! You guessed.")
    return is_guessed


def game():
    # for terminal clearing
    print('\033c')
    print(logo)
    print("Welcome to The GuessGame!\n")

    attempts_count = 5
    hidden_number = new_hidden_number()
    print("I thought a number  between 1 and 100. Try to guess!")

    difficulty = input(
        "Choose a difficulty. Type 'easy' or 'hard'. As you like? [hard] ")
    if difficulty == 'easy':
        attempts_count = 10
    else:
        print("Do you like hardcore. I understand:)")

    print(f"You have {attempts_count} attempts.")

    is_guessed = False
    while not is_guessed:
        if attempts_count > 0:
            guess = int(input("\nYour guess: "))
            attempts_count -= 1
            is_guessed = guess_result(hidden_number, guess)
        else:
            is_guessed = True
            print("\nThis time you couldn't guess.")
            print("Start a new game and I hope you guess my number.")

    is_new_game = input("\nDo you wanna play a new game? [y/N] ").lower()
    if is_new_game == 'y':
        game()

game()

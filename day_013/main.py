import random
from art import logo, vs, crown
from game_data import data


def clear_and_logo():
    print('\033c')
    print(logo)


def print_info(letter, obj):
    print(f" {letter}. {obj['name']}")
    print(f"{obj['description']} from {obj['country']}")


def print_lose_end(score, obj1, obj2):
    print(f"{obj1['name']} has {obj1['follower_count']}M followers.")
    print(f"{obj2['name']} has {obj2['follower_count']}M followers.")
    print(f"\nYour score: {score}.\n")


def print_win_end(score):
    print(crown)
    print(f"\nYour score: {score}.\n")


def game():
    random.shuffle(data)

    data_count = len(data)
    current = 0
    is_continue = True
    score = 0
    is_win = False
    while is_continue:
        # for terminal clearing
        clear_and_logo()

        fact1 = data[current]
        print_info("A", fact1)

        print(vs)

        fact2 = data[current + 1]
        print_info("B", fact2)

        is_higher = fact1["follower_count"] >= fact2["follower_count"]
        is_hl = input(
            f"\nWho has more followers? [A or B] ").lower() == 'a'

        if is_higher == is_hl:
            score += 1
            current += 1
        else:
            is_continue = False
            is_win = False

        if current == data_count-1:
            is_continue = False
            is_win = True

    clear_and_logo()
    if is_win:
        print_win_end(score)
    else:
        print_lose_end(score, fact1, fact2)

    is_new_game = input("Do you wanna play again?[y/N] ").lower() == 'y'
    if is_new_game:
        game()


game()

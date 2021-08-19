############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import logo

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_card():
    """ return random card from deck """
    return random.choice(deck)


def sum_in_hand(cards):
    """ return sum points in player hands"""
    sum_points = 0
    for card in cards:
        sum_points += card
    eleven_count = cards.count(11)
    if eleven_count > 0 and sum_points > 21:
        sum_points -= eleven_count * 10
    return sum_points


def compare_sums(user_cards, comp_cards):
    """ comspare sum of decks """
    user_sum = sum_in_hand(user_cards)
    comp_sum = sum_in_hand(comp_cards)
    return user_sum - comp_sum


def game():
    # for terminal clearing
    print('\033c')
    print(logo)

    user_cards = []
    comp_cards = []

    # add 2 cards
    for _ in range(1, 3):
        user_cards.append(get_card())
        comp_cards.append(get_card())

    print(f"Comp has the first card {user_cards[0]}.")
    # user takes
    is_another = True
    while is_another:
        print(f"You have {user_cards}, {sum_in_hand(user_cards)} points.")
        question = input("Do you want to take another card? [y/N] ").lower()
        if question == 'y':
            another_card = get_card()
            user_cards.append(another_card)
            if sum_in_hand(user_cards) > 21:
                is_another = False
        else:
            is_another = False

    if sum_in_hand(user_cards) > 21:
        print("YOU LOSE.")
    else:
        # comp takes
        while sum_in_hand(comp_cards) < 18:
            comp_cards.append(get_card())

        if sum_in_hand(comp_cards) > 21:
            print("YOU WIN.")
        else:
            # compare sums and result game
            result = compare_sums(user_cards, comp_cards)
            if result > 0:
                print("YOU WIN.")
            elif result < 0:
                print("YOU LOSE.")
            else:
                print("DRAW.")

    # outpur results
    print(f"You: {user_cards}, {sum_in_hand(user_cards)} points.")
    print(f"Comp: {comp_cards}, {sum_in_hand(comp_cards)} points. ")

    # new game
    is_new_game = input("\nDo you want play a new game? [y?N] ").lower()
    if is_new_game == 'y':
        game()

game()

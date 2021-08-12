rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

items = [rock, paper, scissors]

comp_choose = random.randint(0, 2)

player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if player_choose > 2 or player_choose < 0:
    print("Please, type only 0, 1 or 2")
else:

    print("Your choose:")
    print(items[player_choose])

    print("Computer choose:")
    print(items[comp_choose])

    if player_choose > comp_choose:
        if player_choose == 1 or comp_choose == 1:
            print("You win")
        else:
            print("You lose")
    elif player_choose < comp_choose:
        if player_choose == 1 or comp_choose == 1:
            print("You lose")
        else:
            print("You win")
    else:
        print("dead heat")
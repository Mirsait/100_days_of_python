from art import logo


print(logo)
print("Welcome to the secret auction program! ")
bidders = {}

is_input = True

def find_max_bid():
    max_name = ''
    max_bid = 0
    for name in bidders:
        bid = bidders[name]
        if bid > max_bid:
            max_name = name
            max_bid = bid
    print(f"The winner is {max_name} with a bid of ${max_bid}")

while is_input:
    user_name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    bidders[user_name] = bid

    is_other = input("Are there any other bidders? [y/n] ")

    if is_other == 'n':
        is_input = False
    else:
        # for terminal clearing
        print('\033c')
        print(logo)

find_max_bid()



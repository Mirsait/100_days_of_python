# Coffee Machine
from data import MENU, resources
from art import machine, big_cup


def get_ingredients(drink: str) -> dict:
    return MENU[drink]["ingredients"]


def get_cost(drink: str) -> float:
    return MENU[drink]["cost"]


def hello():
    """ Clear and print logo"""
    print('\033c')
    print(machine)
    print("Welcome to The Smart Coffee Machine!")


def print_menu():
    """Display the menu"""
    print("\nMENU")
    for drink in MENU:
        cost = MENU[drink]["cost"]
        print(f"> {drink}: {cost}")


def print_report():
    print("\nReport:")
    for item in resources:
        print(f"| {item}: {resources[item]}")
    print("\n")


def choose_drink() -> str:
    drinks = ", ".join(list(MENU.keys()))
    while True:
        item = input(f"What would you like? ({drinks}): ")
        if item in MENU.keys() or item == "off":
            print(f"You choose {item}.\n")
            return item


def is_resource_enough(drink: str) -> str:
    ingredients = get_ingredients(drink)
    for ingredient in ingredients:
        need_amount = ingredients[ingredient]
        res_amount = resources[ingredient]
        if res_amount < need_amount:
            return ingredient
    return None


def add_to_money(cents: int):
    dollars = cents * 0.01
    if "money" in resources.keys():
        resources["money"] += dollars
    else:
        resources["money"] = dollars


def insert_coins(cost: float) -> bool:
    money_cents = 0
    cost_cents = cost * 100
    print(f"Please, insert coins: ${cost}\n")
    print("* only coins of 1, 5, 10 and 25 cents are accepted.")
    print("* enter 'c' to finish. \n")

    is_interrupted = False
    while money_cents < cost_cents and not is_interrupted:

        rest = cost_cents - money_cents
        choose = input(f"Insert (${rest/100:.2f}): ")

        if choose in ['1', '5', '10', '25']:
            cents = int(choose)
            money_cents += cents
        else:
            is_interrupted = True

    if is_interrupted:
        diff = cost_cents - money_cents
        if diff > 0:
            print(f"\nRefund money: {money_cents} cents.")
    else:
        diff = money_cents - cost_cents
        if diff > 0:
            print(f"\nRefund money: {diff} cents.")
        money_cents -= diff
        add_to_money(money_cents)

    return money_cents >= cost_cents and not is_interrupted


def make_coffee(drink: str):
    ingredients = get_ingredients(drink)
    for item in ingredients:
        amount = ingredients[item]
        resources[item] -= amount


def get_coffee(drink: str):
    print(f"Here is your {drink} ☕.")


def off():
    print('\033c')
    print(big_cup)
    print("The Coffee Machine is off.")


def coffee_machine():
    is_off = False
    hello()
    print_menu()
    print_report()

    drink = choose_drink()
    if drink != "off":
        lack = is_resource_enough(drink)
        if not lack:
            cost = get_cost(drink)
            result = insert_coins(cost)
            if result:
                make_coffee(drink)
                get_coffee(drink)
            else:
                print("Sorry that's not enough money. Money refunded.\n")
        else:
            print(f"Sorry there is not enough {lack}.\n")

        print_report()
        input("Enter to continue ... ")
    else:
        is_off = True

    if is_off:
        off()
    else:
        coffee_machine()


coffee_machine()

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    is_on = True
    menu = Menu()
    accountant = MoneyMachine()
    maker = CoffeeMaker()

    while is_on:
        print('\033c')
        choice = input(f"What would you like? {menu.get_items()}")
        if choice == "report":
            maker.report()
            accountant.report()
        elif choice == "off":
            is_on = False
        else:
            drink = menu.find_drink(choice)
            if drink:
                if maker.is_resource_sufficient(drink):
                    is_paid = accountant.make_payment(drink.cost)
                    if is_paid:
                        maker.make_coffee(drink)

        input("Enter to continue ...")


coffee_machine()

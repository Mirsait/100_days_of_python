from mimath import operations
from art import logo

def calculator():
    # for terminal clearing
    print('\033c')
    print(logo)

    number1 = float(input("What is the first number? "))
    is_calc = True
    while is_calc:
        for operation in operations:
            print(operation, end=" ")
        operation = input("\nWhat operation do you wanna apply? ")
        action = operations[operation]

        number2 = float(input("What is the next number? "))

        result = action(number1, number2)

        print(f"{number1} {operation} {number2} = {result}")

        question = input(f"Type 'y' to continue calculation with {result}, 'n' to new calculation, 'q' to exit: ")
        if question == 'y':
            number1 = result
        elif question == 'n':
            is_calc = False
            calculator()
        else:
            is_calc = False

calculator()

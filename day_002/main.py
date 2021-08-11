# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print("Welcome to Tip Calculator")

total_bill = float(input("What was the total bill? "))

percent = int(input("What persentage tip would you like to give? 10, 12 or 15? "))

people_count = int(input("How many people to split the bill? "))

pay = total_bill / people_count * (1 + percent * 0.01)

message = f"Each person should pay: {pay:.2f}"

print(message)

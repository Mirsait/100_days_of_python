
# Your Life in Weeks

age = input("What is your current age? ")

ages_left = 90 - int(age)
days = ages_left * 365
weeks = ages_left * 52
months = ages_left * 12

text = f"You have {days} days, {weeks} weeks, and {months} months left."

print(text)

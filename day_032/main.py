import os
from datetime import datetime
import pandas
import smtplib
import random

smtp_from = "smtp.gmail.com"
address_from = "your_email@gmail.com"
password_from = "your_password"
default_port = 587  # TLS
TEMPLATES_FOLDER = "letter_templates"


def send_email(address_to, topic, message):
    with smtplib.SMTP(host=smtp_from, port=default_port) as connection:
        connection.starttls()
        connection.login(user=address_from, password=password_from)
        connection.sendmail(
            from_addr=address_from,
            to_addrs=address_to,
            msg=f"Subject:{topic}\n\n{message}"
        )


def get_letter_template():
    files = os.listdir(TEMPLATES_FOLDER)
    file = random.choice(files)
    with open(file=f"{TEMPLATES_FOLDER}/{file}", mode='r') as file:
        letter = file.read()
        return letter


data = pandas.read_csv("birthdays.csv", sep=';').to_dict('records')

today = datetime.today()

for user_data in data:
    birth_date = (int(user_data['month']), int(user_data['day']))

    if birth_date == (today.month, today.day):

        letter_template = get_letter_template()
        new_letter = letter_template.replace('[NAME]', user_data['name'])

        send_email(user_data['email'], "Happy Birthday!", new_letter)

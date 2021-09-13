" Upcoming Weather Alert "

import requests
from datetime import datetime
import smtplib

# email info
EMAIL_USER = ""
EMAIL_PASSWORD_APP = ""
EMAIL_HOST = "smtp.mail.yahoo.com"  # for example

# open weather maps info
OWM_API_KEY = ""
OWM_URL = "https://api.openweathermap.org/data/2.5/onecall"

# request params
parameters = {
    "lat": 30.9754,
    "lon": 52.4345,
    "exclude": "current,minutely,daily,alerts",
    "units": "metric",
    "appid": OWM_API_KEY,
}


def send_email(message):
    with smtplib.SMTP(host=EMAIL_HOST, port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_USER,
                         password=EMAIL_PASSWORD_APP)
        connection.sendmail(
            from_addr=EMAIL_USER,
            to_addrs=EMAIL_USER,
            msg=f"Subject:Bring an umbrella.\n\n{message}")


def load_weather_new_data():
    response = requests.get(OWM_URL, params=parameters)
    data = response.json()
    return data


def create_message_from_data(data):
    hourly = data["hourly"][:12]
    messages = ""
    for hour in hourly:
        weather = hour["weather"][0]
        cond_code = weather["id"]
        if cond_code < 700:
            main = weather["main"]
            description = weather["description"]
            dtime = datetime.fromtimestamp(hour["dt"]).isoformat()
            message = f"Bring an umbrella {dtime} - {main} ({description})\n"
            messages += message
    return messages


data = load_weather_new_data()
messages = create_message_from_data(data)
if len(messages) > 0:
    send_email(messages)

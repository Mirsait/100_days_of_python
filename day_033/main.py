import time
import requests
from datetime import datetime
import smtplib

EMAIL = ""
PASSWORD_APP = ""
SERVER_SMTP = "smtp.mail.yahoo.com"  # for example

MY_LAT = 52.420848  # Your latitude
MY_LONG = 30.995178  # Your longitude


def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return(iss_latitude, iss_longitude)


sun_api_parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def get_sun_hours():
    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=sun_api_parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return (sunrise, sunset)


def send_email():
    with smtplib.SMTP(host=SERVER_SMTP, port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD_APP)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Look up!\n\nThe ISS is over your head."
        )


print("start tracking...")


while True:

    time.sleep(60)

    (iss_lat, iss_long) = get_iss_position()
    # Your position is within +5 or -5 degrees of the ISS position.
    is_near_me = abs(iss_lat - MY_LAT) <= 5 and abs(iss_long - MY_LONG) <= 5

    if is_near_me:
        print(f"iss: [{iss_lat}, {iss_long}]")
        time_now = datetime.now()
        (sunrise, sunset) = get_sun_hours()

        is_dark_now = time_now.hour >= sunset or time_now.hour <= sunrise

        if is_dark_now:
            send_email()

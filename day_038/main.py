
from datetime import datetime
import requests

sheety_endpoint = ""

sheety_header = {
    "Authorization": "Basic ***",
    "Content-Type": "application/json"
}

NUTRI_KEY = ""
NUTRI_ID = ""
nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutri_header = {
    "x-app-id": NUTRI_ID,
    "x-app-key": NUTRI_KEY,
    "Content-Type": "application/json"
}


def create_exercises(lause: str):
    nutri_data = {
        "query": lause,
        "gender": "male",
        "weight_kg": 85,
        "height_cm": 174,
        "age": 34
    }
    response = requests.post(url=nutri_endpoint, json=nutri_data, headers=nutri_header)
    response.raise_for_status()
    exercises = response.json()["exercises"]
    return exercises


def create_sheety_row(data):
    response = requests.post(url=sheety_endpoint, headers=sheety_header, json=data)
    response.raise_for_status()


now = datetime.now()
answer = input("Tell me which exercises you did: ")
#answer = "ran 5km and swimming 20 min"
exercises = create_exercises(answer)

for exercise in exercises:
    data = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.time().strftime("%H:%M:%S"),
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    create_sheety_row(data)

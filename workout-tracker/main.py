import os
import sys
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

sys.path.insert(1, '//wsl$/Ubuntu/home/logan/Development/code/passwords')
import work_out_tracker

APP_KEY = os.environ["MY_APP_ID"]
API_KEY = work_out_tracker.keys("api")
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_headers = {
    "x-app-id": APP_KEY,
    "x-app-key": API_KEY,
}

# so they can insert a type of exercise:
exercise_input = input("Tell me which exercises you did: ")

exercise_params = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": 86.2,
    "height_cm": 182.88,
    "age": 35
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_headers)
response.raise_for_status()
result = response.json()

# Datetime for logging the date and time of the exercise in Google Sheets
today = datetime.today()
date = f"{today.day}/{today.month}/{today.year}"
time = f"{today.hour}:{today.minute}"

# # Sheets GET
sheets_endpoint = "https://api.sheety.co/1573f3f4ff5a0dc8d4bf8c064a9b195a/myWorkouts/workouts"

# basic authentication
basic = HTTPBasicAuth(USERNAME, PASSWORD)

sheets_get = requests.get(url=sheets_endpoint, auth=basic)
sheets_get.raise_for_status()
sheets_get_data = sheets_get.json()

# # Sheets POST
post_params = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": result["exercises"][0]["user_input"],
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"]
    }
}
sheets_post = requests.post(url=sheets_endpoint, json=post_params, auth=basic)
sheets_post.raise_for_status()
sheets_post_data = sheets_post.json()


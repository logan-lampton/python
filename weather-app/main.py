import requests
import sys

# # importing api key to avoid putting them directly in the file
sys.path.insert(1, '//wsl$/Ubuntu/home/logan/Development/code/passwords')
import open_weather_api
api_key = open_weather_api.api_key()

# nyc_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=New%20York&appid={api_key}")

five_day_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"

parameters = {
    "lat": "40.712776",
    "lon": "-74.005974",
    "appid": api_key,
    "cnt": "16",
    "units": "imperial"
}

five_day_response = requests.get(five_day_endpoint, params=parameters)
five_day_response.raise_for_status()

five_day_data = five_day_response.json()

print(five_day_data)
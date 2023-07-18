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


def bring_umbrella():
    weather_ids = []
    # grab the first 4 entries, to simulate 12 hours (as each entry is for 3 hours)
    for entry in five_day_data["list"][:4]:
        for weather_condition in entry["weather"]:
            weather_id = weather_condition["id"]
            # weather ids for rainy weather are less than 600, but also accounts for sleet in the 600s
            if 602 < weather_id < 620 or weather_id < 600:
                weather_ids.append(weather_id)
    # if any rainy weather is true, then returns that we should bring an umbrella
    if weather_ids:
        return "Bring an umbrella today"


print(five_day_data)


print(bring_umbrella())

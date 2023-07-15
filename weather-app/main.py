import requests

api_key = "47b73f61d741abc5d272a3a6d3a9ae2d"

# nyc_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=New%20York&appid={api_key}")

five_day_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"

parameters = {
    "lat": "40.712776",
    "lon": "-74.005974",
    "appid": api_key,
    "cnt": "16"
}

five_day_response = requests.get(five_day_endpoint, params=parameters)

five_day_data = five_day_response.json()

print(five_day_data)
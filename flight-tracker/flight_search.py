#This class is responsible for talking to the Flight Search API.
import requests
import sys
from datetime import datetime, timedelta

from flight_data import FlightData

sys.path.insert(1, '//wsl$/Ubuntu/home/logan/Development/code/passwords')
import flight_tracker

endpoint = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = flight_tracker.keys("api")

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
six_months_from_now = (datetime.now() + timedelta(days=6 * 30)).strftime("%d/%m/%Y")


class FlightSearch:
        def get_destination_code(self, city_name):
            # TEQUILA API data
            headers = {"apikey": TEQUILA_API_KEY}
            query = {
                "term": city_name,
                "location_types": "city"
            }
            response = requests.get(url=f"{endpoint}/locations/query", headers=headers, params=query)
            data = response.json()
            code = data["locations"][0]["code"]
            return code

        def search_prices(self, arrival_airport_code):
            headers = {"apikey": TEQUILA_API_KEY}
            query = {
                "fly_from": "NYC",
                "fly_to": arrival_airport_code,
                "date_from": tomorrow,
                "date_to": six_months_from_now,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "USD"
            }
            response = requests.get(url=f"{endpoint}/v2/search", headers=headers, params=query)
            response.raise_for_status()

            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"No flights found for {arrival_airport_code}")
                return None

            flight_data = FlightData(
                price=data["price"],
                departure_airport_code=data["route"][0]["flyFrom"],
                departure_city=data["route"][0]["cityFrom"],
                destination_airport_code=data["route"][0]["flyTo"],
                destination_city=data["route"][0]["cityTo"],
                depart_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data







import requests
from pprint import pprint

#This class is responsible for talking to the Google Sheet.
endpoint = "https://api.sheety.co/1573f3f4ff5a0dc8d4bf8c064a9b195a/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    # 2. Now use the Sheety API to GET all the data in that sheet and print it out.
    def get_destination_data(self):
        response = requests.get(url=endpoint)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

# 6. In the DataManager Class make a PUT request and use the row id from sheet_data to update the Google Sheet with
# the IATA codes. (Do this using code). HINT: Remember to check the checkbox to allow PUT requests in Sheety.
    def update_iata_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

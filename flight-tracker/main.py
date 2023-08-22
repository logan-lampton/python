#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()

# Check if sheet_data contains any values for the "iataCode" key. If not, then the IATA Codes column is empty in the
# Google Sheet. In this case, pass each city name in sheet_data one-by-one to the FlightSearch class.

# For now, the FlightSearch class can respond with "TESTING" instead of a real IATA code. You should use the response
# from the FlightSearch class to update the sheet_data dictionary.
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_iata_codes()


notification_manager = NotificationManager()

for destination in sheet_data:
    flight = flight_search.search_prices(
        arrival_airport_code=destination["iataCode"]
    )

    if flight and flight.price is not None and flight.price < destination["lowestPrice"]:
        message = f"Low price alert! Only ${flight.price} to fly from {flight.departure_city}-{flight.departure_airport_code} to {flight.destination_city}-{flight.destination_airport_code}, from {flight.depart_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        notification_manager.send_message(message)

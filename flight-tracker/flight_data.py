class FlightData:
    def __init__(self, price, departure_airport_code, departure_city, destination_airport_code, destination_city,
                 depart_date, return_date, stop_overs=0, via_city=""):
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        self.destination_airport_code = destination_airport_code
        self.destination_city = destination_city
        self.depart_date = depart_date
        self.return_date = return_date

#       optional
        self.stop_overs = stop_overs
        self.via_city = via_city








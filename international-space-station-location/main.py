import requests
# the requests module can return the response errors and exceptions

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

# can tap into the data like any other Python dictionary
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

# creating a tuple for the iss position using the longitude and latitude values from the response
iss_position = (longitude, latitude)
print(iss_position)
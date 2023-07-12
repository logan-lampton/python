import requests
# the requests module can return the response errors and exceptions
import smtplib
import sys
import datetime as dt
import time

my_lat = 40.770204
my_lng = -73.930714


# check if ISS is at my position -5 or +5 degrees latitude or longitude
def is_iss_overhead():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    data_iss = response_iss.json()

    # can tap into the data like any other Python dictionary
    iss_lat = data_iss["iss_position"]["latitude"]
    iss_lng = data_iss["iss_position"]["longitude"]

    # check if ISS is at my position -5 or +5 degrees latitude or longitude
    if my_lat - 5 <= iss_lat <= my_lat + 5 and my_lng - 5 <= iss_lng <= my_lng + 5:
        return True


# check if it is night (between sunset and sunrise) in my location
def is_night():
    # sunset and sunrise API
    # lat and lng parameters needed for the get request
    parameters = {
        "lat": my_lat,
        "lng": my_lng,
        "formatted": 0
    }

    response_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()

    data_sun = response_sun.json()

    # sunrise and sunset in 24 hour time; converted from UTC to EST
    sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0]) - 4
    sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0]) + 24 - 4

    # getting current time in my location
    time_now = dt.datetime.now()
    current_hour = time_now.hour

    # check if it is night (between sunset and sunrise) in my location
    if sunset < current_hour < sunrise:
        return True


# importing emails and passwords to avoid putting them directly in the file
sys.path.insert(1, '//wsl$/Ubuntu/home/logan/Development/code/passwords/')
import googlesmtp

# variables for emails and password
my_email = googlesmtp.passwords('gmail')
password = googlesmtp.passwords('gmail_password')
second_email = googlesmtp.passwords('yahoo')



# sending email if night and ISS is overhead
while True:
    start_time = time.time()
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            # login to email
            connection.login(user=my_email, password=password)
            # who the email is from/to; the subject and body of the email
            connection.sendmail(
                from_addr=my_email,
                to_addrs=second_email,
                msg=f"Subject:ISS Overhead\n\n The ISS is overhead. Look up!"
            )
        # code to run every 60 seconds
        time.sleep(60.0 - ((time.time() - start_time) % 60.0))

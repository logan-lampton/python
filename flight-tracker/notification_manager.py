from twilio.rest import Client
import sys

sys.path.insert(1, '//wsl$/Ubuntu/home/logan/Development/code/passwords')
import flight_tracker

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    account_sid = flight_tracker.keys("account")
    auth_token = flight_tracker.keys("auth_token")
    client = Client(account_sid, auth_token)

    def send_message(self, message):
        message = self.client.messages.create(
            from_=flight_tracker.keys("from"),
            to=flight_tracker.keys("to"),
            body=message
        )
        print(message.sid)

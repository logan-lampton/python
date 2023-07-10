import datetime as dt
import random
import smtplib
import sys

# using datetime.now() to get current time and day of week
now = dt.datetime.now()
day_of_week = now.weekday()

# importing emails and passwords to avoid putting them directly in the file
sys.path.insert(1, '//wsl$/Ubuntu/home/logan/Development/code/passwords/')
import googlesmtp

# variables for emails and password
my_email = googlesmtp.passwords('gmail')
password = googlesmtp.passwords('gmail_password')
second_email = googlesmtp.passwords('yahoo')

if day_of_week == 0:
    with open('quotes.txt', encoding="utf-8") as quotes:
        all_quotes = quotes.readlines()
        random_quote = random.choice(all_quotes)
    # SMTP establishing connection and set up to close after running using the with keyword
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        # login to email
        connection.login(user=my_email, password=password)
        # who the email is from/to; the subject and body of the email
        connection.sendmail(
            from_addr=my_email,
            to_addrs=second_email,
            msg=f"Subject:Motivational Monday\n\n{random_quote}"
        )

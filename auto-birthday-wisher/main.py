import smtplib
import sys
import pandas as pd
import datetime as dt
import random

# # importing emails and passwords to avoid putting them directly in the file
sys.path.insert(1, '//wsl$/Ubuntu/home/logan/Development/code/passwords/')
import googlesmtp

# variables for emails and password
my_email = googlesmtp.passwords('gmail')
password = googlesmtp.passwords('gmail_password')
# second_email = googlesmtp.passwords('yahoo')

# get the current month and day
now = dt.datetime.now()
month = now.month
day = now.day

# # Check if today matches a birthday in the birthdays.csv
birthdays = pd.read_csv('birthdays.csv')
for i, birthday in birthdays.iterrows():
    if birthday['month'] == month and birthday['day'] == day:
        # If true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
        # from birthdays.csv
        with open("letter_templates/letter_1.txt") as letter_1, open("letter_templates/letter_2.txt") as letter_2, open("letter_templates/letter_3.txt") as letter_3:
            letter_list = [letter_1, letter_2, letter_3]
            random_letter = random.choice(letter_list)
            random_letter_content = random_letter.readlines()
            random_letter_content[0] = f"Dear {birthday['name']}, \n"
            formatted_random_letter = ''.join(random_letter_content)
            # Send the letter generated to that person's email address.
            # SMTP establishing connection and set up to close after running using the with keyword
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                # login to email
                connection.login(user=my_email, password=password)
                # who the email is from/to; the subject and body of the email
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=f"{birthday['email']}",
                    msg=f"Subject:Happy Birthday!\n\n {formatted_random_letter}"
                )

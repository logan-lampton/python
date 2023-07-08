import smtplib

my_email = "dummyemail@gmail.com"
password = "dummypassword321"
connection = smtplib.SMTP("smtp.gmail.com")
second_email = "dummyemail@yahoo.com"

connection.starttls()

connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=second_email, msg="Hello")
connection.close()


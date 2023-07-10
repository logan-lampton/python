import datetime as dt
# using datetime class to get the current time object with now()
now = dt.datetime.now()
# now.year is an integer
year = now.year
# now has many properties, including month, weekday, microsecond, and much more
# weekday starts at 0, so 0 == Monday
day_of_week = now.weekday()

# dummy data to show the minimum necessary values to set a datetime object
date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)
import pandas as pd

data = pd.read_csv("weather_data.csv")

data_dict = data.to_dict()
# print(data_dict)
temperature_list = data["temp"].to_list()

# grabbing the temp column and averaging the temps, via Python methods

# # average_temp = round(sum(temperature_list) / len(temperature_list), 1)
# # print(average_temp)

# grabbing the temp column and averaging the temps, via pandas methods
# average_temp = data["temp"].mean()
# print(average_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)

# print a row
# monday = data[data.day == "Monday"]
# print(monday)

# finding the highest temperature and returning the row for that day of the week
# day_of_max_temp = data[data.temp == data.temp.max()]
# print(day_of_max_temp)

# # print Monday's temperature in Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp_c = monday.temp
#
# def celsius_to_fahrenheit(temperature):
#     return temperature * 9 / 5 + 32
#
# monday_temp_f = celsius_to_fahrenheit(monday_temp_c)


# how to print a dictionary as a table
dataframe = pd.DataFrame(data_dict)
print(dataframe)

# # how to create a new file
# data.to_csv("example_data.csv")


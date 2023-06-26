import csv
with open("weather_data.csv") as weather_data_file:
    data = csv.reader(weather_data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

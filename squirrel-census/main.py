# Log the total number of squirrels of each color
# Build a new dataframe of the color of squirrels and number of each

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_names = data["Primary Fur Color"].unique()
gray_s = data["Primary Fur Color"].value_counts()["Gray"]
cinnamon_s = data["Primary Fur Color"].value_counts()["Cinnamon"]
black_s = data["Primary Fur Color"].value_counts()["Black"]

color_dataframe = pd.DataFrame(data={"Primary Fur Color": color_names[1::], "Number of Squirrels": [gray_s, cinnamon_s, black_s]})



color_dataframe.to_csv("squirrel_colors.csv")
print(color_dataframe)
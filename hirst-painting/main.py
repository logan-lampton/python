# import colorgram
#
# colors = colorgram.extract('hirst.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     new_color = (red, green, blue)
#     rgb_colors.append(new_color)

from turtle import Turtle, Screen, colormode
import random

color_list = [(233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61),
    (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71),
    (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49),
    (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188),
    (34, 151, 210), (65, 66, 56)]

# 10 x 10 rows of spots
# dots are 20 in size
# dots are spaced 50 apart

hirst = Turtle()
hirst.speed("fast")
colormode(255)
hirst.penup()
hirst.goto(-240, -225)
hirst.hideturtle()

y = -225

for _ in range(10):
    for _ in range(10):
        random_color = random.choice(color_list)
        hirst.dot(20, random_color)
        hirst.fd(50)
        y += 5
    hirst.setx(-240)
    hirst.sety(y)


screen = Screen()
screen.screensize(200000, 150000)
screen.exitonclick()
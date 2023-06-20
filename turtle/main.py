from turtle import Turtle, Screen, colormode
import random
# if it's an installed library, we could shorten it like:
# import turtle as t

timmy = Turtle()
timmy.shape("turtle")
timmy.color("medium spring green")

# --- square ---
# for _ in range(4):
#     timmy.right(90)
#     timmy.forward(100)

# --- dashed line ---
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# --- draw triangle through decagon ---
# i = 3
# colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
#
# while i < 11:
#     angle = 360 / i
#     rand_color = random.choice(colors)
#     timmy.pencolor(rand_color)
#     for _ in range(i):
#         timmy.right(angle)
#         timmy.forward(100)
#     i += 1

# --- random walk ---
# colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
# directions = [0, 90, 180, 270]
#
#
# def random_walk():
#     timmy.speed("fast")
#     timmy.pensize(10)
#     rand_color = random.choice(colors)
#     timmy.pencolor(rand_color)
#     direction = random.choice(directions)
#     timmy.setheading(direction)
#     timmy.forward(30)
#
#
# for _ in range(200):
#     random_walk()


# --- random walk, random colors ---
#
# colormode(255)
# directions = [0, 90, 180, 270]
#
#
# def random_color():
#     red = random.randint(0, 255)
#     blue = random.randint(0, 255)
#     green = random.randint(0, 255)
#     r_color = (red, blue, green)
#     return timmy.pencolor(r_color)
#
#
# def random_walk():
#     timmy.speed("fast")
#     timmy.pensize(10)
#     random_color()
#     direction = random.choice(directions)
#     timmy.setheading(direction)
#     timmy.forward(30)
#
#
# for _ in range(200):
#     random_walk()

# --- spirograph ---
colormode(255)
def random_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    r_color = (red, blue, green)
    return timmy.pencolor(r_color)

timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        random_color()
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.screensize(2000, 1500)
screen.exitonclick()

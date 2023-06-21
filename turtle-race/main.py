from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=750, height=550)

guess = screen.textinput("prompt", "Who will win the race? Enter a color: ").lower()

colors_list = ["purple", "blue", "green", "yellow", "orange", "red"]

turtles = []

def create_turtles():
    for color in colors_list:
        turtle = Turtle(shape='turtle')
        turtle.color(color)
        turtles.append(turtle)


def set_places():
    y = 225

    for turtle in turtles:
        turtle.penup()
        turtle.setpos(-350, y)
        y -= 90


winner = ""
def race():
    global winner
    racing = True
    while racing:
        for turtle in turtles:
            movement_forward = random.randint(5, 25)
            turtle.forward(movement_forward)
            turtle.xcor()
            if turtle.xcor() >= 345:
                racing = False
                winner = turtle.pencolor()


create_turtles()
set_places()
race()
screen.exitonclick()


print(f"{winner.capitalize()} turtle wins!")
if guess == winner:
    print(f"You guessed the winner correctly! You and {winner} turtle have a party!")
else:
    print(f"Too bad, {guess} turtle didn't win; you lose!")

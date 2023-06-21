from turtle import Turtle, Screen

etch = Turtle()
screen = Screen()

def move_right():
    etch.forward(10)

def move_left():
    etch.backward(10)

def counter_clockwise():
    etch.left(10)

def clockwise():
    etch.right(10)

def clear():
    etch.clear()
    etch.reset()


screen.listen()
screen.onkey(fun=move_right, key="w")
screen.onkey(fun=move_left, key="s")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear, key="space")

screen.exitonclick()

# s = backwards
# a = turn counter-clockwise
# d = turn clockwise
# c = clear; position back in center

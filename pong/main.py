from turtle import Screen
from paddle import Paddle

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

# Create and move player paddle
right_paddle = Paddle(x_cord=250, y_cord=0)
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")

# Create another paddle
left_paddle = Paddle(x_cord=-250, y_cord=0)
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")
screen.update()


# Create the ball and make it move

# Detect collision with wall, then bounce

# Detect collision with paddle

# Detect when a paddle misses

# Keep score with a scoreboard

screen.exitonclick()
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

game_is_on = True

# Create and move player paddle
right_paddle = Paddle(x_cord=350, y_cord=0)
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")


# Create another paddle
left_paddle = Paddle(x_cord=-350, y_cord=0)
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")


# Create the ball and make it move
ball = Ball()


while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect collision with wall, then bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with right paddle / left paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()



# Detect when a paddle misses

# Keep score with a scoreboard


screen.exitonclick()
from turtle import Screen
from snake import Snake
import time

# Screen setup
screen = Screen()
screen.setup(width=750, height=750)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create snake body
snake = Snake()

# Control the snake
#  up, down, right, left arrows
screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")

# Move the snake
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



# if new_x >= 345 or new_x <= -345 or new_y >= 345 or new_y <= -345:
#     game_is_on = False

#




# Detect collision with food


# Create scoreboard


# Detect collision with wall


# Detect collision with tail


screen.exitonclick()
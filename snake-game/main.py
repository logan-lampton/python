from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create snake body
snake = Snake()
# Create food
food = Food()
# Create scoreboard
scoreboard = Scoreboard()

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
# Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.track_score()
        scoreboard.update_scoreboard()
        snake.extend()
    # Detect collision with wall
    if snake.head.xcor() >= 335 or snake.head.xcor() <= -335 or snake.head.ycor() >= 335 or snake.head.ycor() <= -335:
        game_is_on = False
        scoreboard.game_over()
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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

scoreboard = Scoreboard()


while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Detect collision with wall, then bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with right paddle / left paddle
    elif ball.distance(right_paddle) < 55 and ball.xcor() > 320 or ball.distance(left_paddle) < 55 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect when right paddle misses
    elif ball.xcor() > 380:
        scoreboard.left_player_score()
        ball.begin_round()
        # if scoreboard.player_one_score + scoreboard.player_two_score > 5:

    # Detect when left paddle misses
    elif ball.xcor() < -380:
        scoreboard.right_player_score()
        ball.begin_round()
    # Keep score with a scoreboard
    scoreboard.update_scoreboard()
    if scoreboard.player_one_score > 9:
        scoreboard.winner = "Player 1"
        scoreboard.game_over()
        game_is_on = False
    elif scoreboard.player_two_score > 9:
        scoreboard.winner = "Player 2"
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(fun=player.move, key="Up")
    car_manager.create_car()
    car_manager.move_cars()
    # Cars are randomly generated
    if player.ycor() >= player.finish_position:
        player.level_up()
        scoreboard.increase_score()
        scoreboard.display_score()
        car_manager.increase_speed()
    # When a turtle collides with a car everything stops and it is game over
    for car in car_manager.all_cars:
        if player.distance(car) <= 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()








from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RANDOM_CHANCE = (1, 7)


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.random_chance = RANDOM_CHANCE

    def create_car(self):
        random_chance_of_car = random.randint(self.random_chance[0], self.random_chance[1])
        if random_chance_of_car == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(1, 2)
            car.setheading(180)
            car.color(random.choice(COLORS))
            car.setpos(280, random.randint(-250, 250))
            self.all_cars.append(car)


    # Cars move from the right edge of the screen to the left edge

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    # Cars increase in speed as the levels increase

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        self.random_chance = (self.random_chance[0], self.random_chance[1] - 1)

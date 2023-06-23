from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.setpos(STARTING_POSITION)
        self.finish_position = FINISH_LINE_Y

    # The turtle (player) moves forwards when the "Up" key is pressed. It can ONLY move forwards
    def move(self):
        self.forward(MOVE_DISTANCE)

# When the turtle hits the top edge of the screen it moves back to the original position and the character levels up

    def level_up(self):
        self.setpos(STARTING_POSITION)


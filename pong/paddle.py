from turtle import Turtle, Screen

screen = Screen()
screen.listen()


class Paddle(Turtle):
    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.penup()
        self.setpos(x_cord, y_cord)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if self.ycor() < 230:
            new_y = self.ycor() + 50
            self.sety(new_y)

    def down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 50
            self.sety(new_y)

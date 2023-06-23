from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(-270, 260)
        self.level = 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

    def increase_score(self):
        self.level += 1

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", False, align="center", font=FONT)

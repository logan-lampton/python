from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')

# Create scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.setpos(-15, 320)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    # Display score
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Hi-Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    # Keep track of score
    def track_score(self):
        self.score += 1

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


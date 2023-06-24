from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')

# Create scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(-15, 320)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.high_score = 0
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
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.setpos(0, 0)
    #     self.write(f"GAME OVER\n Press 'r' to restart", move=False, align=ALIGNMENT, font=FONT)

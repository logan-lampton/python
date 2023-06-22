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
        self.update_scoreboard()

    # Keep track of score
    def track_score(self):
        self.score += 1

    # Display score
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

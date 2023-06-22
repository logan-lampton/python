from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(0, 220)
        self.color("white")
        self.hideturtle()
        self.player_one_score = 0
        self.player_two_score = 0
        self.winner = ""
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.player_one_score} | {self.player_two_score}",
                   move=False, align=ALIGNMENT, font=FONT)

    def right_player_score(self):
        self.player_one_score += 1
        self.update_scoreboard()

    def left_player_score(self):
        self.player_two_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER {self.winner} wins", move=False, align=ALIGNMENT, font=FONT)
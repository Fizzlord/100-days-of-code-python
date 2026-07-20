from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(-0, 270)
        self.pencolor("white")
        self.score = 0
        self.write_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def write_score(self):
        self.write(f"Score is {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self,):
        self.home()
        self.write("Game Over!", align=ALIGNMENT, font=FONT)
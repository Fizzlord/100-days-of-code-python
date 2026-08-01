from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 25, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.pencolor("white")
        self.score1 = 0
        self.score2 = 0
        self.goto(0, 445)
        self.write_score()

    def write_score(self):
        self.write(f"{self.score1} Score {self.score2}", align=ALIGNMENT, font=FONT)

    def update_score(self, ball):
        if ball.xcor() >= 915:
            self.clear()
            self.score2 += 1
            self.write_score()
        elif ball.xcor() <= -915:
            self.clear()
            self.score1 += 1
            self.write_score()
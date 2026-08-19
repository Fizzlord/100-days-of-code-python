FONT = ("Curious", 14, "bold")
ALIGNMENT = "center"
from turtle import Turtle, Screen

screen = Screen()
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.pencolor("black")
        self.level = 1
        self.goto(0, 265)
        self.write_level()

    def write_level(self):
        self.write(f"Level {self.level}", align=ALIGNMENT, font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)

from turtle import Turtle
SIZE_OF_PAD = 50
PADDLE_BORDER = 450


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.pu()
        self.shapesize(stretch_wid=10, stretch_len=1)
        self.goto(position, 0)

    def move_up(self):
        if self.ycor() <= 400:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() >= -400:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

    def listen(self, a, b):
        self.screen.listen()
        self.screen.onkeypress(self.move_up, a)
        self.screen.onkeypress(self.move_down, b)
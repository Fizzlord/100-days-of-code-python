from turtle import Turtle

class MiddleWall(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.pu()
        self.goto(0, 465)
        self.pensize(5)
        self.setheading(270)
        for num in range(50):
            if num % 2 == 0:
                self.pu()
            else:
                self.pd()
            self.fd(20)
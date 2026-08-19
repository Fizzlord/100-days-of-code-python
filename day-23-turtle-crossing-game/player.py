from turtle import Turtle, Screen
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 255


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.shape("turtle")
        # self.color("black")
        self.pu()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.fd(10)

    def move(self):
        self.screen.onkey(self.move_up, "w")

    def win(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        return False
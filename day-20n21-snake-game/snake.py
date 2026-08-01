from turtle import Turtle, Screen

class Snake:

    def __init__(self):
        self.screen = Screen()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in range(15):
            self.add_segment(position)

    def extend(self):
        self.add_segment(-1) #because we are adding it at end of segment

    def add_segment(self, position):
        self.segments.append(Turtle(shape="square"))
        self.segments[position].pu()
        self.segments[position].color("white")
        if position != 0:
            previous_x_cor = self.segments[position - 1].xcor() - 20
            self.segments[position].teleport(previous_x_cor, y=0)

    def listen(self):
        self.screen.listen()
        self.screen.onkey(self.move_left, "a")
        self.screen.onkey(self.move_right, "d")
        self.screen.onkey(self.move_up, "w")
        self.screen.onkey(self.move_down, "s")

    def move(self):

        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
        self.head.fd(20)

    def wall(self):
        pass

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)





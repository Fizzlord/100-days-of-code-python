from turtle import Turtle
WIDTH = 1800
Y = 490
class Wall:

    def __init__(self, location):
        self.location = location
        self.wall = []
        self.make_wall()

    def make_wall(self):
        for brick in range(int(WIDTH/20)):
            self.wall.append(Turtle(shape="square"))
            self.wall[brick].color("white")
            self.wall[brick].pu()
            if brick == 0:
                self.wall[brick].goto(-890, self.location)
            else:
                self.wall[brick].goto(self.wall[brick - 1].xcor() + 20, self.location)
from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.random_direction = random.choice((10, -10))
        self.x_move = self.random_direction
        self.y_move = self.random_direction
        self.move_speed = 0.01


    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)
        self.collision_wall()
        if self.xcor() <= -925 or self.xcor() >= 925:
            self.goto(0, 0)
            self.x_move *= -1
            self.move_speed = 0.01

    def collision_wall(self):
        if self.ycor() <+ -460 or self.ycor() >= 455:
            self.y_move *= -1

    def collision_pad(self, seg):
        if self.distance(seg) <= 100:
            if self.xcor() >= 860 or self.xcor() <= -865:
                self.x_move *= -1
                self.move_speed *= 0.9
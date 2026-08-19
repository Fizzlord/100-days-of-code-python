from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

ENDLINE = -310

class CarManager:

    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_increment = 5
        self.make_speed = 5

    def make_car(self):
        random_make = random.randint(1, self.make_speed)
        if random_make == self.make_speed:
            pos = len(self.cars)
            self.cars.append(Turtle())
            self.cars[pos].pu()
            # self.cars[pos].goto(20, 20)
            self.cars[pos].shape("square")
            self.cars[pos].shapesize(stretch_wid=1, stretch_len=2)
            self.cars[pos].color(random.choice(COLORS))
            self.cars[pos].goto(x=320, y=random.randrange(-240, 240, 20))
            self.cars[pos].setheading(180)
        # self.move()

    def lose(self, player):
        if len(self.cars) != 0:
            for car in self.cars:
                if car.distance(player) < 20:
                    return True
        return False

    def move(self):

        for car in self.cars:
            if car.xcor() >= ENDLINE:
                car.fd(self.move_increment)

    def increase_speed(self):
        self.move_increment += 5
        self.make_speed -= 1

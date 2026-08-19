import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
scoreboard = Scoreboard()
screen.tracer(0)
player = Player()
car = CarManager()
screen.listen()
player.move()

time_delay = 0.05



game_is_on = True
while game_is_on:
    if player.win():
        scoreboard.update_level()
        car.increase_speed()

    car.move()
    car.make_car()
    if car.lose(player):
        scoreboard.game_over()
        game_is_on = False
    time.sleep(time_delay)
    screen.update()


screen.exitonclick()
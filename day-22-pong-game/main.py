from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from wall import Wall
from ball import Ball
from middle_wall import MiddleWall
import time

screen = Screen()
screen.setup(width=1800, height=1000)
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True

scoreboard = Scoreboard()
ball = Ball()
wall1 = Wall(-485)
wall2 = Wall(490)
middle_wall = MiddleWall()
# paddle1 = Paddle(-880)
# paddle2 = Paddle(875)
screen.update()
r_paddle = Paddle(-880)
l_paddle = Paddle(875)
r_paddle.listen("w", "s")
l_paddle.listen("Up", "Down")

while game_is_on:
    scoreboard.update_score(ball)
    ball.move()

    ball.collision_pad(r_paddle)
    ball.collision_pad(l_paddle)
    screen.update()

    time.sleep(ball.move_speed)



screen.exitonclick()
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

game_is_on = True
snake.listen()


while game_is_on:
    time.sleep(0.1)
    snake.move()
    screen.update()



    if snake.head.distance(food) < 15:
        food.refresh()
        screen.update()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if abs(snake.head.xcor()) >= 300 or abs(snake.head.ycor()) >= 300:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with itself
    seg_pos = []
    for seg in range(1, len(snake.segments)):
        seg_pos.append(snake.segments[seg].position())
    if snake.head.position() in seg_pos:
        scoreboard.game_over()
        game_is_on = False
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.game_over()
            game_is_on = False












screen.exitonclick()
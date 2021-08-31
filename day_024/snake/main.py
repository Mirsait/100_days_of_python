""" The snake game"""

from scoreboard import Scoreboard
from food import Food
from snake import Snake
from turtle import Screen
import time
import files

WIDTH = 600
HEIGHT = 600

files.create_file()
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = Scoreboard(pos_x=0, pos_y=HEIGHT/2 - 40)

snake = Snake()

food = Food(screen_w=WIDTH, screen_h=HEIGHT)

screen.listen()
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.set_random_position(WIDTH-15, HEIGHT-15)
        scoreboard.add_point()
        snake.extend()

    # detect wall
    is_x = snake.head.xcor() > WIDTH/2 or snake.head.xcor() < -WIDTH/2
    is_y = snake.head.ycor() > HEIGHT/2 or snake.head.ycor() < -HEIGHT/2

    if is_x or is_y:
            scoreboard.reset()
            snake.reset()

    # self-killing
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

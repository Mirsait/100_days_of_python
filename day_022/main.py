from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
from turtle import Screen
import time

WIDTH = 800
HEIGHT = 600
START_POSITION = [(-WIDTH//2+40, 0), (WIDTH//2-40, 0)]
MAX_COUNT = 5


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

scoreboard = Scoreboard((0, HEIGHT//2 - 60))
left_paddle = Paddle(START_POSITION[0])
left_paddle.color("red")
right_paddle = Paddle(START_POSITION[1])
ball = Ball()


def on_left_up():
    left_paddle.move_up()


def on_left_down():
    left_paddle.move_down()


def on_right_up():
    right_paddle.move_up()


def on_right_down():
    right_paddle.move_down()


def wall_collision():
    """ collision of a ball with a wall """
    if ball.ycor() > HEIGHT / 2 - 20 or ball.ycor() < -HEIGHT / 2 + 20:
        ball.bounce_y()
    # ball was missed
    elif ball.xcor() > WIDTH/2 - 20:
        scoreboard.add_left()
        ball.reset_position()
    elif ball.xcor() < -WIDTH/2 + 20:
        scoreboard.add_right()
        ball.reset_position()


def paddle_collision(ball: Ball, paddle: Paddle):
    """collision of a ball with a paddle"""
    if ball.distance(paddle) < 50 and abs(ball.xcor()) > abs(paddle.xcor())-20:
        ball.color(*paddle.color())
        ball.add_velocity()
        ball.bounce_x()


def paddle_restriction(paddle: Paddle):
    """ limiting the movement of the paddle between walls"""
    if paddle.ycor() > HEIGHT/2-50:
        paddle.setpos(paddle.xcor(), HEIGHT/2-50)
    elif paddle.ycor() < -HEIGHT/2 + 50:
        paddle.setpos(paddle.xcor(), -HEIGHT/2+50)


screen.onkey(on_left_up, 'w')
screen.onkey(on_left_down, 's')
screen.onkey(on_right_up, 'Up')
screen.onkey(on_right_down, 'Down')
screen.listen()

is_game_on = True
while is_game_on:
    time.sleep(0.017)
    screen.update()
    ball.move()
    wall_collision()
    paddle_collision(ball, right_paddle)
    paddle_collision(ball, left_paddle)
    paddle_restriction(left_paddle)
    paddle_restriction(right_paddle)

    if scoreboard.score_right == MAX_COUNT or scoreboard.score_left == MAX_COUNT:
        is_game_on = False

scoreboard.game_over()


screen.exitonclick()

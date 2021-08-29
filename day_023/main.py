import random
from street import Street
import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600

half_width = WIDTH // 2
half_height = HEIGHT // 2

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

street = Street(street_width=HEIGHT - 100,
                street_length=WIDTH, count_stripes=20)
scoreboard = Scoreboard(position=(-half_width+25, half_height - 50))
player = Player()
manager = CarManager()


def get_random_position():
    r_x = half_width + 15
    ys = [x for x in range(-half_height+50, half_height -
                           50, (HEIGHT - 100)//20)]
    r_y = random.choice(ys)
    return (r_x, r_y)


screen.listen()
screen.onkey(player.move, "Up")


def is_collide(player: Player, car: Turtle):
    return player.distance(car) < 30


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    manager.add_car(get_random_position())
    manager.move()

    if player.ycor() > half_height:
        player.to_start()
        scoreboard.add_level()
        manager.increase_speed()

    for car in manager.cars:
        if car.xcor() < -half_width:
            car.clear()
            car.ht()
        elif is_collide(player, car):
            scoreboard.sub_live()
            player.to_start()

    if scoreboard.lives == 0:
        game_is_on = False


scoreboard.game_over()
screen.exitonclick()

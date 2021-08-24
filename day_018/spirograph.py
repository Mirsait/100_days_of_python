""" drawing spirograph """

import turtle as t
import random

tim = t.Turtle()

t.colormode(255)

tim.speed(10)

def random_color():
    """get random color """
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


def spirograph(radius: int, steps: int):
    """ draw a spirograph """
    angle = 360 / steps
    color = random_color()
    while steps > 0:
        tim.left(angle)
        tim.pencolor(color)
        tim.circle(radius)
        steps -= 1

spirograph(150, 100)

t.exitonclick()

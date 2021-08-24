""" drawing shapes """
import turtle as t


tim = t.Turtle()


def shape(center_x, center_y, side_length, angle_count):
    """drawing a shape """
    angle = 360 / angle_count
    tim.up()
    tim.setpos(center_x, center_y)
    tim.down()
    for _ in range(angle_count):
        tim.left(angle)
        tim.forward(side_length)


def triangle(center_x, center_y, side_length):
    """ 3 """
    shape(center_x, center_y, side_length, 3)


def square(center_x, center_y, side_length):
    """ 4 """
    shape(center_x, center_y, side_length, 4)


def rectangle(center_x, center_y, width, height):
    """ 4 """
    angle = 90
    tim.up()
    tim.setpos(center_x, center_y)
    tim.down()
    for _ in range(2):
        tim.left(angle)
        tim.forward(height)
        tim.left(angle)
        tim.forward(width)


def pentagon(center_x, center_y, side_length):
    """ 5 """
    shape(center_x, center_y, side_length, 5)


def hexagon(center_x, center_y, side_length):
    """ 6 """
    shape(center_x, center_y, side_length, 6)


def heptagon(center_x, center_y, side_length):
    """ 7 """
    shape(center_x, center_y, side_length, 7)


def octogon(center_x, center_y, side_length):
    """ 8 """
    shape(center_x, center_y, side_length, 8)


def nonagon(center_x, center_y, side_length):
    """ 9 """
    shape(center_x, center_y, side_length, 9)


def decagon(center_x, center_y, side_length):
    """ 10 """
    shape(center_x, center_y, side_length, 10)


def hendecagon(center_x, center_y, side_length):
    """ 11 """
    shape(center_x, center_y, side_length, 11)


def dodecagon(center_x, center_y, side_length):
    """ 12 """
    shape(center_x, center_y, side_length, 12)


def tridecagon(center_x, center_y, side_length):
    """ 13 """
    shape(center_x, center_y, side_length, 13)


def tetradecagon(center_x, center_y, side_length):
    """ 14 """
    shape(center_x, center_y, side_length, 14)


def heptadecagon(center_x, center_y, side_length):
    """ 17 """
    shape(center_x, center_y, side_length, 17)


X0 = 0
Y0 = -50

triangle(X0, Y0, 50)
square(X0, Y0, 50)
rectangle(X0, Y0, 50, 100)
pentagon(X0, Y0, 50)
hexagon(X0, Y0, 50)
heptagon(X0, Y0, 50)
octogon(X0, Y0, 50)
nonagon(X0, Y0, 50)
decagon(X0, Y0, 50)
hendecagon(X0, Y0, 50)
dodecagon(X0, Y0, 50)
tridecagon(X0, Y0, 50)
tetradecagon(X0, Y0, 50)
heptadecagon(X0, Y0, 50)

tim.up()
tim.home()

t.exitonclick()

""" Hirst picture """

import turtle as t
import random
import colorgram


def read_colors():
    """ Extract 6 colors from an image. """
    rgb_colors = colorgram.extract('hirst.jpg', 30)
    colors = []
    for cg in rgb_colors:
        red = cg.rgb.r
        green = cg.rgb.g
        blue = cg.rgb.b
        new_color = (red, green, blue)
        colors.append(new_color)
    return colors


colors = [
    (184, 41, 78), (38, 93, 151), (179, 165, 32),
    (213, 153, 86), (131, 87, 61),
    (229, 69, 51), (203, 76, 129), (83, 109, 201),
    (49, 136, 95), (107, 48, 37), (52, 58, 95), (139, 36, 82),
    (27, 174, 192), (216, 204, 36), (225, 174, 167), (39, 83, 85),
]

PIC_WIDTH = 600
DOT_SIZE = 30
DOT_COUNT = 10 #in row/col

tim = t.Turtle()
t.colormode(255)
t.screensize(canvwidth=PIC_WIDTH, canvheight=PIC_WIDTH, bg=None)
tim.shape('circle')
tim.up()
tim.speed(3)


def draw_hirst(turtle, dot_count: int):
    """ drawing Hirst picture """
    offset = -PIC_WIDTH / 2
    tim.setpos(offset, offset)
    rows = dot_count + 1 # rows = cols
    for row in range(1, rows):
        for col in range(1, rows):
            x = offset + col * PIC_WIDTH / rows
            y = offset + row * PIC_WIDTH / rows
            turtle.setpos(x, y)
            turtle.dot(DOT_SIZE, random.choice(colors))


def draw_border(turtle):
    turtle.setpos(PIC_WIDTH/2, PIC_WIDTH/2)
    turtle.down()
    turtle.pencolor("black")
    turtle.pensize(2)
    for _ in range(4):
        tim.right(90)
        tim.forward(PIC_WIDTH)


draw_hirst(tim, DOT_COUNT)
draw_border(tim)
tim.hideturtle()


t.exitonclick()

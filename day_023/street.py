from turtle import Turtle


def bold_line(turtle, x1, y1, x2, y2):
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.penup()


def dashed_line(turtle, x1, x2, y):
    turtle.goto(x1, y)
    turtle.color("red")
    turtle.setheading(180)
    while turtle.xcor() > x2:
        turtle.pendown()
        turtle.forward(10)
        turtle.up()
        turtle.forward(10)


class Street(Turtle):
    def __init__(self, street_width: int, street_length: int, count_stripes: int):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.street_width = street_width
        self.street_length = street_length
        self.count = count_stripes
        self.bold_bolder()
        self.dashed_lines()

    def bold_bolder(self):
        self.color("black")
        st = self.street_length/2
        sw = self.street_width/2
        self.pensize(4)
        bold_line(self, st, sw, -st, sw)
        bold_line(self, -st, -sw, st, -sw)
        self.pensize(2)
        bold_line(self, st, 2, -st, 2)
        bold_line(self, st, -2, -st, -2)

    def dashed_lines(self):
        line_width = self.street_width / self.count
        st = self.street_length/2
        for i in range(1, self.count):
            line_y = -self.street_width/2 + i*line_width
            dashed_line(self, st, -st, line_y)

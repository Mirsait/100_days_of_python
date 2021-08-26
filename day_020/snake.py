""" Snake module """

from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    """ Snake  class  """

    def __init__(self) -> None:
        self.segments = []
        self.create()
        self.head = self.segments[0]
        self.head.color('red')

    def create(self):
        """ create segments """
        for position in START_POSITIONS:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        """ moving forward """
        for i in range(len(self.segments)-1, 0, -1):
            pos_x = self.segments[i-1].xcor()
            pos_y = self.segments[i - 1].ycor()
            self.segments[i].goto(pos_x, pos_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        """ turn left """
        self.head.left(90)

    def right(self):
        """ turn right """
        self.head.right(90)

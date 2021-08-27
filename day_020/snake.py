""" Snake module """

from turtle import Turtle, position

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
EAST, NORTH, WEST, SOUTH = 0, 90, 180, 270


class Snake:
    """ Snake  class  """

    def __init__(self) -> None:
        self.segments = []
        self.create()
        self.head: Turtle = self.segments[0]
        self.head.color('red')

    def create(self):
        """ create segments """
        for position in START_POSITIONS:
            self.add_segment(position=position)

    def add_segment(self, position):
        """ add segment to position """
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        """ add segment to last position"""
        self.add_segment(self.segments[-1].position())

    def curtail(self):
        """ remove last segment """
        last = len(self.segments)-1
        self.segments[last].clear()
        self.segments[last].ht()
        del self.segments[last]

    def move(self):
        """ moving forward """
        for i in range(len(self.segments)-1, 0, -1):
            pos_x = self.segments[i - 1].xcor()
            pos_y = self.segments[i - 1].ycor()
            self.segments[i].goto(pos_x, pos_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        """ turn left """
        if not self.head.heading() == EAST:
            self.head.setheading(WEST)

    def right(self):
        """ turn right """
        if not self.head.heading() == WEST:
            self.head.setheading(EAST)

    def up(self):
        """ turn up"""
        if not self.head.heading() == SOUTH:
            self.head.setheading(NORTH)

    def down(self):
        """ turn down """
        if not self.head.heading() == NORTH:
            self.head.setheading(SOUTH)


from turtle import Turtle


class Paddle(Turtle):
    """ Paddle class  """

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)

    def move_up(self):
        """ moving up """
        self.setposition(self.xcor(), self.ycor() + 50)

    def move_down(self):
        """ moving down """
        self.setposition(self.xcor(), self.ycor() - 50)

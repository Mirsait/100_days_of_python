import random
from turtle import Turtle


class Food(Turtle):
    """ The food class """

    def __init__(self, screen_w, screen_h):
        super().__init__(shape="circle")
        self.penup()
        self.color("yellow")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed(10)
        self.set_random_position(screen_w, screen_h)

    def set_random_position(self, width, height):
        offset = 15
        rand_x = random.randint(-width//2 + offset, width//2 - offset)
        rand_y = random.randint(-height//2 + offset, height//2 - offset)
        self.setposition(rand_x, rand_y)

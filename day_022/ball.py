from turtle import Turtle

START_VELOCITY = 4


class Ball(Turtle):
    """ Ball class """

    def __init__(self):
        super().__init__("square")
        self.penup()
        self.color("gray")
        self.home()
        self.velocity_x = START_VELOCITY
        self.velocity_y = START_VELOCITY - 2

    def move(self):
        """ moving with velocity """
        new_x = self.xcor() + self.velocity_x
        new_y = self.ycor() + self.velocity_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        """ bounce along the Y axis """
        self.velocity_y *= -1

    def bounce_x(self):
        """ bounce along the X axis """
        self.velocity_x *= -1

    def reset_position(self):
        """ go home, bounceX and reset velocity """
        self.home()
        sign = 1
        if self.velocity_x > 0:
            sign = -1
        self.velocity_x = START_VELOCITY * sign
        self.velocity_y = START_VELOCITY * sign - 2


    def add_velocity(self):
        """ add speed: step = 0.2  """
        plus = 0.2
        if self.velocity_x > 0:
            self.velocity_x += plus
        else:
            self.velocity_x -= plus

        if self.velocity_y > 0:
            self.velocity_y += plus
        else:
            self.velocity_y -= plus

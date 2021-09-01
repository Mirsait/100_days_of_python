from turtle import Turtle

FONT = ("Verdana", 8, "normal")


class Disposer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        # self.hideturtle()
        self.color('red')
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def print_to_position(self, text: str, x: int, y: int):
        self.setposition(x, y)
        self.write(text, move=False, align='center', font=FONT)
        self.setposition(x, y-5)

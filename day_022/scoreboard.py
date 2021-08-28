from turtle import Turtle

# FONT = ("Roboto Black", 24, "normal")
FONT = ("GamePower", 48, "normal")
ALIGNMENT = "center"
FONT_OVER = ("GamePower", 72, "normal")


class Scoreboard(Turtle):
    """ Scoreboard class """

    def __init__(self, position):
        super().__init__()
        self.setposition(position)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score_left = 0
        self.score_right = 0
        self.draw()

    def draw(self):
        """ display scores"""
        self.clear()
        score_text = f"{self.score_left} : {self.score_right}"
        self.write(score_text, False, ALIGNMENT, FONT)

    def add_left(self):
        """ add one point to left player"""
        self.score_left += 1
        self.draw()

    def add_right(self):
        """ add one point to right player"""
        self.score_right += 1
        self.draw()

    def game_over(self):
        """ display game over screen/text"""
        self.home()
        self.clear()
        winner = "RIGHT"
        if self.score_left > self.score_right:
            winner = "LEFT"
            self.color("red")
        message = f"{winner}\n-\nwinner!"
        self.write(message, False, ALIGNMENT, FONT_OVER)

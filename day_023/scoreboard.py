from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """ Scoreboard class """

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("darkgray")
        self.setposition(position)
        self.level = 0
        self.lives = 3
        self.draw()

    def draw(self):
        self.clear()
        text = f"Level: {self.level}\nLives: {self.lives}"
        self.write(text, move=False, align="left", font=FONT)

    def add_level(self):
        self.level += 1
        self.draw()

    def sub_live(self):
        self.lives -= 1
        self.draw()

    def game_over(self):
        self.home()
        self.color("black")
        text = f"GAME OVER"
        self.write(text, move=False, align="center", font=FONT)

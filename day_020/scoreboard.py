from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 20, "normal")


class Scoreboard(Turtle):
    """ Scoreboard """

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.score = 0
        self.setposition(pos_x, pos_y)
        self.color("white")
        self.draw()
        self.hideturtle()

    def draw(self):
        self.clear()
        score_text = f"score: {self.score}"
        self.write(arg=score_text, move=False, align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.draw()

    def subtract_point(self):
        self.score -= 1
        self.draw()

    def game_over(self):
        self.home()
        self.clear()
        self.color('red')
        text = f"GAME OVER!\nScore: {self.score}"
        self.write(arg=text, move=False, align=ALIGNMENT, font=FONT)

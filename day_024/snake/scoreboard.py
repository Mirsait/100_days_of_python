from turtle import Turtle
import files

ALIGNMENT = "center"
FONT = ("Verdana", 20, "normal")


class Scoreboard(Turtle):
    """ Scoreboard """

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.score = 0
        self.high_score = files.get_high_score()
        self.setposition(pos_x, pos_y)
        self.color("white")
        self.update_board()
        self.hideturtle()

    def update_board(self):
        self.clear()
        score_text = f"score: {self.score}\t high: {self.high_score}"
        self.write(arg=score_text, move=False, align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.update_board()

    def subtract_point(self):
        self.score -= 1
        self.update_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            files.save_score(self.high_score)
        self.score = 0
        self.update_board()

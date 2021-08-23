""" Question """


class Question:
    """ Class of quiz question """

    def __init__(self, text: str, answer: bool):
        self.text = text
        self.answer = answer

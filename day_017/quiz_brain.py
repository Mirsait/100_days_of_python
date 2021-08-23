""" QuizBrain """


class QuizBrain:
    """ Class for QuizGame"""

    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.answer_list = []
        self.score = 0

    def next_question(self):
        """ Performs a game step: asks a question, increases the score """
        current_question = self.question_list[self.question_number]
        number = self.question_number + 1
        user_answer = input(f"Q.{number}.{current_question.text}.(True/False)")
        self.check_answer(current_question.answer, user_answer)
        self.question_number += 1
        print(f"Your current score: {self.score}/{self.question_number}.\n")

    def still_has_questions(self) -> bool:
        """ Checks if there are any more questions """
        return self.question_number < len(self.question_list)

    def check_answer(self, correct_answer: str, user_answer: str):
        """ Compare user answer and correct answer """
        if correct_answer.lower() == user_answer.lower():
            self.score += 1
            print("You are right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}.")

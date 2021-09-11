import html
from question_model import Question

class QuizBrain:

    def __init__(self, q_list: list[Question]):
        self.question_number: int = 0
        self.score: int = 0
        self.question_list: list[Question] = q_list
        self.current_question: Question = self.question_list[self.question_number]

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {text}"

    def check_answer(self, user_answer: str):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        return False

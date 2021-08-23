""" Entry point """

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

print('\033c')

questions = []

for item in question_data:
    new_q = Question(item["question"], item["correct_answer"])
    questions.append(new_q)

brain = QuizBrain(questions)

while brain.still_has_questions():
    brain.next_question()

print("You have complete the quiz.")
print(f"Your final score: {brain.score}/{brain.question_number}.\n")

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for question in question_data:
    entry = Question(question["text"], question["answer"])
    question_bank.append(entry)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()



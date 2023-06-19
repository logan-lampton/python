from question_model import Question
from data import question_data

question_bank = []


for question in question_data:
    entry = Question(question["text"], question["answer"])
    question_bank.append(entry)

print(question_bank[0].text)

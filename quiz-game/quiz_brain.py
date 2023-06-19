# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if the quiz is over

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        self.question_number += 1
        input(f"Q.{self.question_number}: {self.question_list[self.question_number].text} (True/False)?" )


# MOCK DISPLAY
# Q.1: A slug's blood is green. (True/False)?
# Q.{question_number}: {entry["Text"]}. (True/False)?
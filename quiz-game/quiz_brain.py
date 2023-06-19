# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if the quiz is over

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?" )
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You're right! 😁")
            self.score += 1
        else:
            print("Sorry, you got it wrong 😟")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")

# MOCK DISPLAY
# Q.1: A slug's blood is green. (True/False)?

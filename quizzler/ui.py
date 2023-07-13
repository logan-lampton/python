from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", foreground="white", background=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)
        self.q_text = self.canvas.create_text(150, 125, text="Test", font=("Arial", 18, "italic"), fill=THEME_COLOR,
                                              width=275)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.select_true)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.select_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        next_q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.q_text, text=next_q_text)

    def select_true(self):
        self.get_next_question()

    def select_false(self):
        self.get_next_question()


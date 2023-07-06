import random
from tkinter import *
import pandas as pd
from random import *

# ---------------------------- DATA FOR FLASH CARDS ------------------------------- #

data = pd.read_csv("data/french_words.csv")
word_data = data.to_dict(orient="records")
initial_choice = choice(word_data)
initial_word = initial_choice["French"]
current_language = "French"


# ---------------------------- CREATE NEW FLASH CARDS ------------------------------- #


def next_card():
    current_card = choice(word_data)
    while current_card == initial_choice:
        current_card = choice(word_data)
    word_label.config(text=current_card["French"])


# ---------------------------- UI SETUP --------------------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Language Flash Cards")

# Card
frame = Frame(width=800, height=526)
frame.grid(column=0, columnspan=2, row=0)

card_front = PhotoImage(file="images/card_front.png")
front_card = Label(frame, image=card_front, background=BACKGROUND_COLOR)
front_card.grid(column=0, row=0)

language_label = Label(frame, text=current_language, background="white", font=("Ariel", 40, "italic"))
language_label.place(x=250, y=100)

word_label = Label(frame, text=initial_word, background="white", font=("Ariel", 60, "bold"))
word_label.place(x=250, y=223)

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

checkmark_img = PhotoImage(file="images/right.png")
right_button = Button(image=checkmark_img, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)


window.mainloop()

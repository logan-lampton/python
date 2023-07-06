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
    canvas.itemconfig(word_text, text=current_card["French"])


# ---------------------------- FLIP FLASH CARDS ------------------------------------- #




# ---------------------------- UI SETUP --------------------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Language Flash Cards")

# Card

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, columnspan=2, row=0)

card_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)

card_back = PhotoImage(file="images/card_back.png")

language_text = canvas.create_text(400, 150, text=current_language, font=("Ariel", 40, "italic"))

word_text = canvas.create_text(400, 263, text=initial_word, font=("Ariel", 60, "bold"))

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

checkmark_img = PhotoImage(file="images/right.png")
right_button = Button(image=checkmark_img, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)


window.mainloop()

import random
from tkinter import *
import pandas as pd
from random import *
import os

# ---------------------------- DATA FOR FLASH CARDS --------------------------------- #

# Open the words to learn file if it exists
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")

word_data = data.to_dict(orient="records")
current_card = {}

# --------------------------------- RESET DATA -------------------------------------- #


def reset_data():
    global data
    try:
        os.remove("data/words_to_learn.csv")
    except FileNotFoundError:
        pass
    data = pd.read_csv("data/french_words.csv")
    get_next_card()


# ---------------------------- CREATE NEW FLASH CARDS ------------------------------- #


def get_next_card():
    global current_card, flip_timer, word_data
    # cancel timer so that it always flips 3 seconds after the latest click
    window.after_cancel(flip_timer)
    # save card data globally
    current_card = choice(word_data)
    # update the canvas to reflect the new data in the correct format
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    # Set new timer
    flip_timer = window.after(3000, card_flip)

# ---------------------------- TRACKING WORDS KNOWN --------------------------------- #


def is_known():
    # remove the word from the list of words, so it is not repeated
    word_data.remove(current_card)
    # Get the next card
    get_next_card()
    # track questions that the user reports getting wrong
    to_learn_data = pd.DataFrame(word_data)
    # index=False prevents Pandas from saving the index number of the element again, each time
    to_learn_data.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- FLIP FLASH CARDS ------------------------------------- #


def card_flip():
    global current_card
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)


# ---------------------------- UI SETUP --------------------------------------------- #


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Language Flash Cards")

# Flip card timer
flip_timer = window.after(3000, card_flip)

# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, columnspan=3, row=0)

card_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)

card_back = PhotoImage(file="images/card_back.png")

language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))

word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=get_next_card)
wrong_button.grid(column=0, row=1)

checkmark_img = PhotoImage(file="images/right.png")
right_button = Button(image=checkmark_img, highlightthickness=0, command=is_known)
right_button.grid(column=2, row=1)

reset_button = Button(text="Reset", fg="white", font=("Ariel", 20), highlightthickness=0, background="#7fb599",
                      command=reset_data)
reset_button.grid(column=1, row=1)

# initial call to populate first card
get_next_card()

window.mainloop()

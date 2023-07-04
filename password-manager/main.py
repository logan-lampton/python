from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():

    # num_of_r_letters = randint(8, 10)
    # num_of_r_numbers = randint(2, 4)
    # num_of_r_symbols = randint(2, 4)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    # newlist = [expression for item in iterable if condition == True]

    password_char_list = password_letters + password_numbers + password_symbols

    shuffle(password_char_list)

    new_password = ''.join(password_char_list)

    password_input.insert(0, new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_value = website_input.get()
    email_value = email_input.get()
    password_value = password_input.get()
    new_data = {
        website_value: {
            "email": email_value,
            "password": password_value,
        }
    }
    print(new_data)
    if len(website_value) == 0 or len(email_value) == 0 or len(password_value) == 0:
        messagebox.showinfo(title="Oops!", message="Please provide values for the website, email, and password")
    else:
        try:
            with open("passwordfile.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("passwordfile.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("passwordfile.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# .insert
# .delete

# Ex: Amazon | logan.dummyemail@email.com | qw3252345


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, padx=10)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(column=1, columnspan=2, row=1, sticky="W")
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, columnspan=2, row=2, sticky="W")
email_input.insert(0, "logan.dummyemail@email.com")

password_input = Entry(width=35)
password_input.grid(column=1, columnspan=2, row=3, sticky="W")

generate_btn = Button(text="Generate Password", width=30, command=generate_password)
generate_btn.grid(column=1, columnspan=2, row=4, sticky="W")

add_btn = Button(text="Add", width=30, command=save)
add_btn.grid(column=1, columnspan=2, row=5, sticky="W")

add_padding = Label(text="", width=18)
add_padding.grid(column=2, row=4)


# grid(row=2, column=0, columnspan=2)


window.mainloop()
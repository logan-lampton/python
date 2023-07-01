from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# def generate_password():
#     new_password =
#     password_input.insert(0, new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_value = website_input.get()
    email_value = email_input.get()
    password_value = password_input.get()
    f = open("passwordfile.txt", "a")
    f.write(f"{website_value} | {email_value} | {password_value} \n")
    website_input.delete(0, END)
    password_input.delete(0, END)
    f.close()

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

generate_btn = Button(text="Generate Password", width=30)
generate_btn.grid(column=1, columnspan=2, row=4, sticky="W")

add_btn = Button(text="Add", width=30, command=save)
add_btn.grid(column=1, columnspan=2, row=5, sticky="W")

add_padding = Label(text="", width=18)
add_padding.grid(column=2, row=4)


# grid(row=2, column=0, columnspan=2)


window.mainloop()
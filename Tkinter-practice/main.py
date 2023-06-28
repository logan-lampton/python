import tkinter
# don't need to write tkinter in the class calls if imported as:
# from tkinter import *

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
# or written as:
my_label.config(text="New Text")
# must use, pack, place or grid, or it won't appear on the screen
# my_label.place(x=0, y=0)
# my_label.pack()
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Entry
input = tkinter.Entry(width=12)
input.grid(column=3, row=2)
# input.pack()

# Button
def button_clicked():
    user_input = input.get()
    my_label["text"] = user_input


button = tkinter.Button(text="Click me!", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)


new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# CAN'T have grid and pack in the same project

window.mainloop()

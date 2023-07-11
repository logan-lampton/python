from tkinter import *
import requests


# API call
def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text=data["quote"])

# GUI
window = Tk()
window.title("Kanye says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=350, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(200, 200, image=background_img)
quote_text = canvas.create_text(200, 200, text="", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()
window.mainloop()

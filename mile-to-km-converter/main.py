from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=600, height=325)
window.config(padx=100, pady=100)

miles_input = Entry(width=12)
miles_input.grid(column=2, row=1)

miles_label = Label(text="Miles", font=("Arial", 24))
miles_label.grid(column=3, row=1)
miles_label.config(padx=10, pady=10)

equal_to_label = Label(text="is equal to", font=("Arial", 24))
equal_to_label.grid(column=1, row=2)
equal_to_label.config(padx=10, pady=10)

output_km = Label(text="0", font=("Arial", 24))
output_km.grid(column=2, row=2)
output_km.config(padx=10, pady=10)

km_label = Label(text="Km", font=("Arial", 24))
km_label.grid(column=3, row=2)
km_label.config(padx=10, pady=10)


def button_click():
    if miles_input.get() == "":
        output_km.config(text=0)
    else:
        m_to_km = round(float(miles_input.get()) * 1.609344, 2)
        output_km.config(text=m_to_km)


calc_button = Button(text="Calculate", command=button_click)
calc_button.grid(column=2, row=3)
calc_button.config(padx=5, pady=5)

window.mainloop()

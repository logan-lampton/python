from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = 0
# count_down_time = WORK_MIN * 60
# pause = False

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global reps, checkmarks
    window.after_cancel(count_down_time)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    checkmarks = 0
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps, checkmarks
    reps += 1
    individual_checkmark = "✔"
    checkmark_label.config(text=f"{individual_checkmark}" * checkmarks)
    # print(reps)
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title_label.config(text="Long Break!", fg=RED)
        checkmarks = 0
        count_down(long_break)
    elif reps % 2 != 0:
        title_label.config(text="Work", fg=GREEN)
        checkmarks += 1
        count_down(work_time)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = math.floor(count % 60)
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count_seconds < 10:
        canvas.itemconfig(timer_text, text=f"{count_minutes}:0{count_seconds}")
    if count > 0:
        global count_down_time
        count_down_time = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- PAUSE ------------------------------- #
# def pause():
#     global pause, count_down_time, type_of_rep
#     if pause == True:
#         start_timer(count_down_time)
#         pause = False
#     else:
#         window.after_cancel(count_down_time)
#         pause = True



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
title_label.grid(column=1, row=0)

checkmark_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(column=1, row=3)

start_btn = Button(text="Start", font=(FONT_NAME, 10), highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", font=(FONT_NAME, 10), highlightthickness=0, command=reset)
reset_btn.grid(column=2, row=2)

# pause_btn = Button(text="Pause", font=(FONT_NAME, 10), highlightthickness=0, command=pause)
# pause_btn.grid(column=1, row=4)


window.mainloop()

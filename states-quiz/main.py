from turtle import Turtle, Screen
import pandas as pd
import string

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

states = Turtle()
screen = Screen()
screen.title("Guess the U.S. States!")

image = "blank_states_img.gif"
screen.addshape(image)
states.shape(image)

# JUST FYI: how to track mouse clicks to grab state coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(fun=get_mouse_click_coor)

data = pd.read_csv("50_states.csv")

correct = 0
guessed_states = []
playing = True

while playing:
    user_answer = string.capwords(screen.textinput(title=f"{correct}/50 states correct",
                                                   prompt="What's another state name?"))
    if user_answer == "Exit":
        # new_list = [new_item for item in list if test]
        missing_states = [state for state in data.state if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    for state in data.state:
        if state == user_answer:
            guessed_states.append(user_answer)
            correct_state = data[data.state == f"{user_answer}"]
            text = Turtle()
            text.penup()
            text.hideturtle()
            text.goto(float(correct_state.x - 15), float(correct_state.y - 5))
            text.write(f"{user_answer}")
            correct += 1

        if correct == 50:
            playing = False
            you_win = Turtle()
            you_win.pen()
            you_win.hideturtle()
            you_win.write("You win, smartypants!")

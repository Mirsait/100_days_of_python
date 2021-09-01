from disposer import Disposer
import turtle
import pandas
import os

DATA_FILE = "50_states.csv"
MAP_IMG = "blank_states_img.gif"
STATES_TO_LEARN = "states_to_learn.csv"


# load data
data = pandas.read_csv(DATA_FILE)
all_states = data["state"].to_list()
states_count = len(all_states)
guessed_states = []

# game window
screen = turtle.Screen()
screen.title("U. S. States Game")
screen.addshape(MAP_IMG)
turtle.shape(MAP_IMG)


def print_state(text, x, y):
    tim = Disposer()
    tim.print_to_position(text, x, y)


is_game_on = True

while is_game_on:

    title = f"U.S. States Game: {len(guessed_states)}/{states_count}"
    answer = turtle.textinput(
        title,  prompt='Enter the name of the state you know').title()

    if answer == "Exit":
        is_game_on = False
        states_to_learn = [
            state for state in all_states if state not in guessed_states]
        pandas.DataFrame(states_to_learn).to_csv(STATES_TO_LEARN)

    elif answer in all_states and answer not in guessed_states:
        state = data[data["state"] == answer]
        x_cor, y_cor = int(state['x']), int(state['y'])
        guessed_states.append(answer)
        print_state(answer, x_cor, y_cor)

    if len(guessed_states) == len(all_states):
        is_game_on = False
        if os.path.exists(STATES_TO_LEARN):
            os.remove(STATES_TO_LEARN)


# turtle.mainloop()

import turtle
import pandas
from location import Location

screen = turtle.Screen()
screen.title("US State Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
is_game_on = True
score = 0

df = pandas.read_csv("50_states.csv")
screen.tracer(0)
while is_game_on:
    answer_state = turtle.textinput(f"{score}/ {50} Guess The State", prompt="What's another State Name?")
    answer_state = answer_state.title()
    if len(df[df.state == answer_state]) == 1:
        x_cor = int(df[df.state == answer_state].x)
        y_cor = int(df[df.state == answer_state].y)
        state = Location(x_cor, y_cor, answer_state)
        score += 1

screen.listen()
turtle.mainloop()

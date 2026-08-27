from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S.A States Game")
states_img = "blank_states_img.gif"
screen.addshape(states_img)
turtle = Turtle(shape=states_img)

## To get coordinate. Already provided so not used here

# def get_mouse_click_coor(x, y):
#     print(x, y)
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()

user_correct_guess = []

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
states_to_learn_list = []


while len(user_correct_guess) <= 50:

    answer_state = screen.textinput(title=f"Guess The {len(user_correct_guess)}/50 State",
                                    prompt="What state does U.S.A have?").title()

    if answer_state == "Exit":
        for state in states_list:
            if state not in user_correct_guess:
                states_to_learn_list.append(state)
        states_to_learn_df = pandas.DataFrame(states_to_learn_list)
        states_to_learn_df.to_csv("states_learn.csv")
        break
    if answer_state in states_list and answer_state not in user_correct_guess:
        user_correct_guess.append(answer_state)
    else:
        continue

    row = data[data.state == answer_state]
    x = row.x.item()
    y = row.y.item()

    pen = Turtle()
    pen.hideturtle()
    pen.pu()
    pen.goto(x, y)
    pen.write(answer_state)
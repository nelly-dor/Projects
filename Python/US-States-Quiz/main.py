import turtle as t
import pandas

#Prep the screen
screen = t.Screen()
screen.title("US States Quiz")
image = "blank_states_img.gif"
screen.setup(width=750, height=500)
screen.addshape(image)
t.shape(image)
t.penup()

#load the csv file and get relevant data
US_data = pandas.read_csv("50_states.csv")
states = US_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    # Display a popup for user input
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Guess another state's name").title()
    #   Save missing states to CSV  if the player needs to leave the game
    if answer_state == "Exit":
        missing_states=[s for s in states if s not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # Evaluate if the user input is a US state
    if answer_state in states:
        guessed_states.append(answer_state)
        row = US_data[US_data.state == answer_state]
        tim = t.Turtle()
        tim.penup()
        tim.hideturtle()
        tim.goto(x=row.x.item(),y=row.y.item())
        tim.write(answer_state)



t.mainloop()

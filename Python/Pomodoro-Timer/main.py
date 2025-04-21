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
CHECK_SIGN = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def resetClicked():
    window.after_cancel(timer)
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    timer_label["text"] = "Timer"
    timer_label["fg"] = GREEN
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def startClicked():
    global reps
    reps += 1
    seconds = 0
    if reps < 8 and reps%2 == 1:
        timer_label["text"] = "Work"
        timer_label["fg"] = RED
        seconds = WORK_MIN*60
    elif reps < 8 and reps%2 == 0:
        timer_label["text"] = "Break"
        timer_label["fg"] = PINK
        seconds = SHORT_BREAK_MIN*60
    elif reps == 8 :
        timer_label["text"] = "Break"
        timer_label["fg"] = GREEN
        seconds = LONG_BREAK_MIN*60
    countdown(seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(seconds):
    #Get minutes/seconds int values
    minInt = math.floor(seconds/60)
    secInt = seconds%60
    #Using the int values to print nicely formatted strings
    min =  f"0{minInt}" if minInt < 10 else f"{minInt}"
    sec = f"0{secInt}" if secInt < 10 else f"{secInt}"
    time = f"{min}:{sec}"
    canvas.itemconfig(timer_text, text=time)
    if seconds > 0 :
        global timer
        timer = window.after(1000, countdown, seconds-1)
    else:
        if reps < 8 and reps%2 == 1:
            checkmark_label.config(text=CHECK_SIGN*(math.floor(reps/2)+1))
        startClicked()

# ---------------------------- UI SETUP ------------------------------- #
#Window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



#Canvas setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photoTomato = PhotoImage(file="tomato.png")
canvas.create_image( 100, 112, image=photoTomato)
timer_text = canvas.create_text(110,130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

#Buttons setup


startButton = Button(text="Start", command= startClicked, highlightthickness=0)
resetButton = Button(text="Reset", command= resetClicked, highlightthickness=0)

#Labels setup

checkmark_label = Label(fg=GREEN, bg=YELLOW)
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)

#Widgets layout
timer_label.grid(column=1, row=0)
startButton.grid(column=0, row=2)
checkmark_label.grid(column=1, row=3)
resetButton.grid(column=2, row=2)

window.mainloop()



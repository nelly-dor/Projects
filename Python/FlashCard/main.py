import tkinter
from helpers.worddictionary import WordDictionary
from helpers.FileManager import FileManager

BACKGROUND_COLOR = "#B1DDC6"
wd = WordDictionary()
fm = FileManager(wd.get_data_dict())
flip_timer = None


#-------Card Management--------------
def nextCard():
    global flip_timer
    if flip_timer != None:
        window.after_cancel(flip_timer)
    lang = "French"
    if canvas.itemcget(title_text_id, "text") != "Welcome":
        fm.removeItem(wd.get_word(lang), lang)

    wd.set_random_index()
    updateUI(lang)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    updateUI("English")

def wrongPressed():
    nextCard()

def windowClosedHandler():
    fm.saveFile()
    global flip_timer
    if flip_timer != None:
        window.after_cancel(flip_timer)
    window.quit()
    window.destroy()

# ------ Update UI --------

def updateUI(title):
    selected_card = card_front if title == "French" else card_back
    fg = "black" if title == "French" else "white"
    canvas.itemconfig(card_image_id, image=selected_card)
    canvas.itemconfig(title_text_id, text = title, fill=fg)
    canvas.itemconfig(word_text_id, text=wd.get_word(title), fill=fg)

# ---- Setup UI -----------
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.protocol("WM_DELETE_WINDOW", windowClosedHandler)

card_front = tkinter.PhotoImage(file="images/card_front.png")
card_back = tkinter.PhotoImage(file="images/card_back.png")
correct = tkinter.PhotoImage(file="images/right.png")
wrong = tkinter.PhotoImage(file="images/wrong.png")

canvas = tkinter.Canvas(width=800, height=526)
card_image_id = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_text_id = canvas.create_text(400, 150, text="Welcome", font=("Arial", 40, "italic"))
word_text_id = canvas.create_text(400, 263, text="Click on checkmark", font=("Arial", 50, "bold"))


correct_btn = tkinter.Button(image=correct, highlightthickness=0, command=nextCard)
wrong_btn = tkinter.Button(image=wrong, highlightthickness=0, command=nextCard)

#--- Widget Layout-------------------------
canvas.grid(row=0, column=0, columnspan=2)
correct_btn.grid(row=1, column=0)
wrong_btn.grid(row=1, column=1)


window.mainloop()




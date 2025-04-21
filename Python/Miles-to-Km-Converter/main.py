from tkinter import *

#Setup the window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

#Entry
entry = Entry(width=10)

#Labels
miles = Label(text="Miles")
km = Label(text="Km")
resultValue = Label(text="0")
equal = Label(text="is equal to")

#Button
def btn_clicked():
    input_val = entry.get()
    resultValue["text"] = f"{int(input_val)*1.60934}"
btn = Button(text="Calculate", command=btn_clicked)

#Display the elements
entry.grid(column=1, row=0)
miles.grid(column=2, row=0)
equal.grid(column=0, row=1)
resultValue.grid(column=1, row=1)
km.grid(column=2, row=1)
btn.grid(column=1,row=2)

#Launch the window loop
window.mainloop()
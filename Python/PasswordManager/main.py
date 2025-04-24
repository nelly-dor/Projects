from tkinter import *
from tkinter import messagebox
from random import choice
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    pwd_str = ''.join([choice(string.ascii_letters+string.digits+string.punctuation) for n in range(12)])
    pwd_entry.insert(0, pwd_str)
    window.clipboard_clear()
    window.clipboard_append(pwd_str)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():
    website = website_entry.get()
    email = email_entry.get()
    password = pwd_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                pwd_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Keeper")
window.config(padx=50, pady=50)

#PhotoImage and canvas
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)

#Label setup
website_label = Label(text="Website:")
email_label=Label(text="Email/Username:")
pwd_label = Label(text="Password:")

#Entry setup
website_entry = Entry(width=35)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.insert(0,"123@123.com")
pwd_entry = Entry(width=17)

#Button setup
genBtn= Button(text="Generate Password", command=generate)
addBtn= Button(text="Add", command=savePassword, width=30)

#Widget layout
website_label.grid(column=0,row=1)
email_label.grid(column=0,row=2)
pwd_label.grid(column=0,row=3)

website_entry.grid(column=1,row=1, columnspan=2)
email_entry.grid(column=1,row=2, columnspan=2)
pwd_entry.grid(column=1,row=3)
genBtn.grid(column=2,row=3)
addBtn.grid(column=1,row=4, columnspan=2)

window.mainloop()
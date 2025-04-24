from tkinter import *
from tkinter import messagebox
from random import choice
import string
import json

#---------------------------- SEARCH PASSWORD ---------------------------------- #
def searchPassword():
    data_dict = []
    website = website_entry.get()
    try:
        with open("data.json", mode="r") as data:
            data_dict = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data_dict:
            email = data_dict[website]["email"]
            password = data_dict[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
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
website_entry = Entry(width=20)
website_entry.focus()
email_entry=Entry(width=38)
email_entry.insert(0,"123@123.com")
pwd_entry = Entry(width=20)

#Button setup
genBtn= Button(text="Generate Password", command=generate)
addBtn= Button(text="Add", command=savePassword, width=30)
searchButton = Button(text="Search", command=searchPassword)

#Widget layout
website_label.grid(column=0,row=1)
email_label.grid(column=0,row=2)
pwd_label.grid(column=0,row=3)

website_entry.grid(column=1,row=1)
email_entry.grid(column=1,row=2, columnspan=2)
pwd_entry.grid(column=1,row=3)
genBtn.grid(column=2,row=3)
addBtn.grid(column=1,row=4, columnspan=2)
searchButton.grid(column=2,row=1)

window.mainloop()
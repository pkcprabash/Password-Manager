from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import pyperclip
import json

def generate_password():
    entry_password.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbol = [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_number = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = password_letter + password_symbol + password_number

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    entry_password.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    json_data = {
        website:{
            "email":email,
            "password":password
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Error", message="Please correct the errors!")

    else:
        is_ok=messagebox.askokcancel(title=website,message=f"Email: {email}\nPassword: {password}\nOk?")


        if is_ok:
            try:
                with open("data.json", "r") as file:
                    datas = json.load(file)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(json_data,file, indent=4)

            else:
                datas.update(json_data)

                with open("data.json", "w") as file:

                    json.dump(datas,file, indent=4)

            finally:
                    entry_password.delete(0, END)
                    entry_website.delete(0, END)


def search_credentials():
    website = entry_website.get()
    try:
        with open("data.json","r") as file:
            content = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found!")
    else:

        if website in content:
            messagebox.showinfo(title=website, message=f"Email: {content[website]['email']}\nPassword: {content[website]['password']}")
        else:
            messagebox.showinfo(title=website, message="There is no credintials saved for this website")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

Photo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthicknes=0)
canvas.create_image(100, 100, image=Photo)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
entry_website = Entry(width=18)
entry_website.grid(row=1, column=1)
entry_website.focus()
button_website_search = Button(text="Search", width = 14, command = search_credentials)
button_website_search.grid(row=1, column=2)

label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)
entry_email = Entry(width=32)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0,"pkc@email.com")

label_password = Label(text="Password: ")
label_password.grid(row=3, column=0)
entry_password = Entry(width=18)
entry_password.grid(row=3, column=1)
button_password = Button(text="Generate Password", width=14, command=generate_password)
button_password.grid(row=3, column=2)

button_add = Button(text="Add", width=33, command = save_password)
button_add.grid(row=4, column=1, columnspan=2)



window.mainloop()
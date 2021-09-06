from json.decoder import JSONDecodeError
import tkinter as tk
from tkinter import messagebox
import password_generator as pg
import pyperclip
import json

# ---------------------------- SAVE PASSWORD ------------------------------- #
FILE_NAME = "data.json"


def generate_password():
    new_pass = pg.generate()
    pyperclip.copy(new_pass)
    entry_pass.delete(0, tk.END)
    entry_pass.insert(0, new_pass)


def save_password():
    web_site = entry_web.get().title()
    login = entry_login.get()
    password = entry_pass.get()

    new_data = {
        web_site: {
            "email": login,
            "password": password
        }
    }

    if len(web_site) == 0 or len(password) == 0:
        messagebox.showinfo("There are blank fields.")
    else:
        message = f"Login: {login} \nPassword: {password}. \nIs this OK?"
        answer = messagebox.askquestion("Save data", message)
        if answer == "yes":
            try:
                with open(FILE_NAME, 'r') as file:
                    data = json.load(file)
            except (FileNotFoundError, JSONDecodeError):
                with open(FILE_NAME, 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open(FILE_NAME, 'w') as file:
                    json.dump(data, file, indent=4)
            finally:
                entry_web.delete(0, tk.END)
                entry_pass.delete(0, tk.END)


def search_site():
    site_search = entry_web.get().title()
    try:
        with open(FILE_NAME, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No Data File Found.")
    except JSONDecodeError:
        messagebox.showinfo("Error", "Data File is empty.")
    else:
        if site_search in data:
            email = data[site_search]["email"]
            password = data[site_search]["password"]
            message = f"Email:  {email} \nPassword:  {password}"
            messagebox.showinfo(site_search, message)
        else:
            messagebox.showinfo(
                site_search, "No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)


canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
pass_image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, row=0)

PADS = {
    "padx": 5,
    "pady": 10,
    "sticky": tk.EW
}
FONT = ("Fira Code", 10, "normal")

# website
lbl_web = tk.Label(text="Website", font=FONT)
lbl_web.grid(column=0, row=1)
entry_web = tk.Entry(font=FONT)
entry_web.grid(column=1, row=1, **PADS)

# search
btn_search = tk.Button(text="Search", command=search_site, font=FONT)
btn_search.grid(column=2, row=1, **PADS)

# e-mail
lbl_login = tk.Label(text="Email/Username", font=FONT)
lbl_login.grid(column=0, row=2)
entry_login = tk.Entry(font=FONT)
entry_login.grid(column=1, row=2, columnspan=2, **PADS)

# password
lbl_pass = tk.Label(text="Password", font=FONT)
lbl_pass.grid(column=0, row=3)
entry_pass = tk.Entry(font=FONT)
entry_pass.grid(column=1, row=3, **PADS)

# generate
btn_generate = tk.Button(text="Generate Password",
                         command=generate_password, font=FONT)
btn_generate.grid(column=2, row=3, **PADS)


# save
btn_save = tk.Button(text="Save", command=save_password, font=FONT)
btn_save.grid(column=1, row=4, columnspan=2, **PADS)

window.mainloop()

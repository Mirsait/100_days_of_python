import tkinter as tk
from tkinter import messagebox
import password_generator as pg
import pyperclip

# ---------------------------- SAVE PASSWORD ------------------------------- #
FILE_NAME = "data.txt"


def generate_password():
    new_pass = pg.generate()
    pyperclip.copy(new_pass)
    entry_pass.delete(0, tk.END)
    entry_pass.insert(0, new_pass)


def save_password():
    web_site = entry_web.get()
    login = entry_login.get()
    password = entry_pass.get()

    message = f"Login: {login} \nPassword: {password}. \nIs this OK?"

    answer = messagebox.askquestion("Save data", message)
    if answer == "yes":
        with open(FILE_NAME, 'a') as file:
            data = f"{web_site} | {login} | {password}\n"
            file.write(data)
        entry_web.delete(0, tk.END)
        entry_pass.delete(0, tk.END)

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
entry_web.grid(column=1, row=1, columnspan=2, **PADS)

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

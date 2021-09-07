import tkinter as tk
import pandas
import random
import os
# ------------- data -----------------

dict_file = "data/words.csv"
words_to_learn = "data/words_to_learn.csv"

if os.path.isfile(words_to_learn):
    dict_file = words_to_learn

df = pandas.read_csv(dict_file, sep=';')
langs = df.keys()
all_words = df.to_dict(orient='records')

print(len(all_words))

current_card = {"": "", "": ""}


def flip_card():
    set_texts(False)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(all_words)
    set_texts()
    flip_timer = window.after(3000, flip_card)


def set_texts(is_front=True):
    if is_front:
        lang = langs[0]
        word = current_card[lang]
        image = card_front_image
        text_color = "black"
    else:
        lang = langs[1]
        word = current_card[lang]
        image = card_back_image
        text_color = "white"
    canvas.itemconfig(card_image, image=image)
    canvas.itemconfig(text_lang, text=lang)
    canvas.itemconfig(text_word, text=word, fill=text_color)


def on_right():
    all_words.remove(current_card)
    pandas.DataFrame(all_words).to_csv(words_to_learn, sep=';', index=False)
    canvas.itemconfig(text_count, text=f"{len(all_words)}")
    next_card()

# ---------------- UI -------------------


BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("langust")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

card_front_image = tk.PhotoImage(file="images/card_front.png")
card_back_image = tk.PhotoImage(file="images/card_back.png")
btn_right_image = tk.PhotoImage(file="images/right.png")
btn_wrong_image = tk.PhotoImage(file="images/wrong.png")

canvas = tk.Canvas(width=800, height=526,
                   background=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

text_lang = canvas.create_text(
    400, 150, text="Title", fill="gray", font=("Arial", 40, "italic"))
text_word = canvas.create_text(
    400, 263, text="word", fill="black", font=("Arial", 40, "bold"))
text_count = canvas.create_text(
    400, 475, text=f"{len(all_words)}", fill="lightgray", font=("Arial", 14, 'normal'))

btn_wrong = tk.Button(image=btn_wrong_image,
                      highlightthickness=0, border=0, command=next_card)
btn_wrong.grid(column=0, row=1)

btn_right = tk.Button(image=btn_right_image,
                      highlightthickness=0, border=0, command=on_right)
btn_right.grid(column=1, row=1)

next_card()
window.mainloop()

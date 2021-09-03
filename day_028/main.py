import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    title_text.config(text="pomodoro", fg="gray")
    lbl_markers.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_text.config(text="break", fg=RED)
        count_down(long_break)
    elif reps % 2 == 0:
        title_text.config(text="break", fg=PINK)
        count_down(short_break)
    else:
        title_text.config(text="work", fg=GREEN)
        count_down(work_time)


def set_marker(count):
    if count % 2 == 0:
        checks = '✓' * (count // 2)
        lbl_markers.config(text=checks)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def seconds_to_strtime(seconds: int) -> str:
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins:02}:{secs:02}"


def count_down(count: int):
    global reps
    global timer
    if count > 0:
        count_text = seconds_to_strtime(count)
        canvas.itemconfig(timer_text, text=count_text)
        timer = window.after(1000, count_down, count-1)
    elif count == 0:
        if reps % 8 == 0:
            reps = 0
            set_marker(reps)
        start_timer()
        set_marker(reps)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

title_style = {
    "font": (FONT_NAME, 27, "normal"),
    "fg": "gray",
    "bg": YELLOW
}
title_text = tk.Label(text="pomodoro", **title_style)
title_text.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)

timer_font = (FONT_NAME, 36, "bold")
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=timer_font)
canvas.grid(column=1, row=1)

btn_style = {
    "background": "white",
    "foreground": 'black',
    "font": (FONT_NAME, 14, "normal"),
    "highlightthickness": 0
}

btn_start = tk.Button(text="start", **btn_style, command=start_timer)
btn_start.grid(column=0, row=2)

btn_reset = tk.Button(text="reset", **btn_style, command=reset_timer)
btn_reset.grid(column=2, row=2)


markers_style = {
    "fg": "green",
    "bg": YELLOW,
    "font": (FONT_NAME, 16, "normal")
}
lbl_markers = tk.Label(text="", **markers_style)
lbl_markers.grid(column=1, row=3)


window.mainloop()

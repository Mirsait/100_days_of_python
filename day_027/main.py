import tkinter as tk
from tkinter.constants import END

FONT = ("Verdana", 12, "normal")


def btn_convert_clicked():
    if window.focus_get() == entry_km:
        km = float(entry_km.get())
        miles = km / 1.61
        entry_ml.delete(0, END)
        entry_ml.insert(0, f"{miles:.2f}")
    elif window.focus_get() == entry_ml:
        miles = float(entry_ml.get())
        km = miles * 1.61
        entry_km.delete(0, END)
        entry_km.insert(0, f"{km:.2f}")


window = tk.Tk()
window.title("Distance Converter")
window.resizable(0, 0)

# paddings around widget
pads = {"padx": 20, "pady": 20}

# kilometers
entry_km = tk.Entry(name="entry_km", font=FONT)
entry_km.grid(column=0, row=0, **pads)
entry_km.focus()

label_km = tk.Label(text="kilometers", font=FONT)
label_km.grid(column=1, row=0, **pads)

# miles
entry_ml = tk.Entry(name="entry_ml", font=FONT)
entry_ml.grid(column=0, row=1, **pads)

label_ml = tk.Label(text="miles", font=FONT)
label_ml.grid(column=1, row=1, **pads)

# button
btn_convert = tk.Button(text="Convert", command=btn_convert_clicked)
btn_convert.grid(column=2, row=0, rowspan=2, **pads)

window.mainloop()

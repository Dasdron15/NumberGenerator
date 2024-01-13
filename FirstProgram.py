import tkinter as tk
from tkinter import CENTER
import random
import string
from ctypes import windll

font_tuple = ("Helvetica", 12, "bold")
second_font = ("Helvetica", 27, "bold")


def generator_sys():
    global invalid
    numbers = string.digits
    num1 = from_num.get()
    num2 = to_num.get()
    invalid.config(text="")

    for k in range(len(numbers)):
        if numbers[k] in num1 and numbers[k] in num2:
            invalid.config(text="")
            num1 = int(num1)
            num2 = int(num2)
            if num1 > num2:
                invalid.config(text="Invalid values")
                invalid.place(relx=0.5, rely=0.5, anchor=CENTER)
            else:
                invalid.config(text=random.randint(num1, num2), fg="black")
        else:
            invalid.config(text="Invalid values")
            invalid.place(relx=0.5, rely=0.5, anchor=CENTER)


win = tk.Tk()
windll.shcore.SetProcessDpiAwareness(1)
win.geometry("300x400")
win.resizable(False, False)
win.title("Number generator")

from_num = tk.Entry(win, width=10)
from_num.place(x=70, y=100)

to_num = tk.Entry(win, width=10)
to_num.place(x=170, y=100)

from_text = tk.Label(win, text="from", font=font_tuple)
from_text.place(x=80, y=70)

to_text = tk.Label(win, text="to", font=font_tuple)
to_text.place(x=190, y=70)

generated_text = tk.Label(win, text="", font=second_font, justify="center")
generated_text.place(relx=0.5, rely=0.5, anchor=CENTER)

invalid = tk.Label(win, text="", justify="center", font=font_tuple, fg="red")

generate = tk.Button(win, text="Generate", command=generator_sys)
generate.place(x=120, y=250)


tk.mainloop()

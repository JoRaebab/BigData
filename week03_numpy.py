import numpy as np
import random
import tkinter as tk  # Built in GUI
from tkinter import messagebox

def click_button():
    try:
        r = int(en_row.get())
        c = int(en_col.get())

        rows= [[random.randint(1, 100) for i in range(r)] for i in range(c)]
        # print(rows)
        matrix = np.array(rows, dtype='int16')
        lbl_result.config(text=matrix)
    except ValueError as err:
        lbl_result.config(text=f"입력 값이 없습니다.\n{err}")
        messagebox.showerror('Error!',f"입력 값이 없습니다.\n{err}")



window = tk.Tk()
window.title('numpy gui version v1.2')
window.geometry('300x150')

# create widget
lbl_result = tk.Label(text="random numpy 2d array")
en_row = tk.Entry()
en_col = tk.Entry()
btn_click = tk.Button(text="click me!", command=click_button)

# widget layout
# lbl_result.place(x=50, y=50)
# btn_click.place(x=0, y=0)
lbl_result.grid(row=0, column=0, columnspan=2)
en_row.grid(row=1, column=0)
en_col.grid(row=1, column=1)
btn_click.grid(row=2, column=0, columnspan=2, sticky=tk.EW)
# lbl_result.pack()
# en_row.pack(fill='x')
# en_col.pack(fill='x')
# btn_click.pack(fill='x')

window.mainloop()
# n = int(input("input number : "))
# l = [random.randint(1, 100) for i in range(n)]
# v = np.array(l, dtype='int16')
# print(v)
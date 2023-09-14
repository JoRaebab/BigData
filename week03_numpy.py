import numpy as np
import tkinter as tk  # Built in GUI
from tkinter import messagebox

# def press_enter_key(ev):
#     click_button()
#     messagebox.showinfo('coordinate value', f"{ev.x}, {ev.y}")

def click_button(*args):
    try:
        r,c = map(int, en_row_col.get().split()) # space bar
        matrix = np.random.randint(1, 101, size=(r,c))
        lbl_result.config(text=matrix)
    except ValueError as err:
        messagebox.showerror('Error!',f"입력 값이 없습니다.\n{err}")



window = tk.Tk()
window.title('numpy gui version v2.0')
window.geometry('300x150')

# create widget
lbl_result = tk.Label(text="random numpy 2d array")
en_row_col = tk.Entry()
btn_click = tk.Button(text="click me!", command=click_button)

# enter key binding with button
# en_row_col.bind("<Return>", press_enter_key)
en_row_col.bind("<Return>", click_button)

# widget layout

lbl_result.pack()
en_row_col.pack(fill='x')
btn_click.pack(fill='x')

en_row_col.focus()

window.mainloop()
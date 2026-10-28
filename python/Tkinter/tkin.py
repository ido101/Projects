from tkinter import *
from math import ceil
screen = Tk()
screen.title("Simple Calculator")
e = Entry(screen, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def add_btn():
    num1 = e.get()
    global first_num
    first_num = int(num1)
    e.delete(0, END)


def clear_btn():
    e.delete(0, END)


def click_btn(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(num))


def equal_btn():
    num2 = e.get()
    e.delete(0, END)
    e.insert(0, first_num + int(num2))


# Define buttons
btn_1 = Button(screen, text="1", padx=40, pady=20, command=lambda: click_btn(1), borderwidth=3)
btn_2 = Button(screen, text="2", padx=40, pady=20, command=lambda: click_btn(2), borderwidth=3)
btn_3 = Button(screen, text="3", padx=40, pady=20, command=lambda: click_btn(3), borderwidth=3)
btn_4 = Button(screen, text="4", padx=40, pady=20, command=lambda: click_btn(4), borderwidth=3)
btn_5 = Button(screen, text="5", padx=40, pady=20, command=lambda: click_btn(5), borderwidth=3)
btn_6 = Button(screen, text="6", padx=40, pady=20, command=lambda: click_btn(6), borderwidth=3)
btn_7 = Button(screen, text="7", padx=40, pady=20, command=lambda: click_btn(7), borderwidth=3)
btn_8 = Button(screen, text="8", padx=40, pady=20, command=lambda: click_btn(8), borderwidth=3)
btn_9 = Button(screen, text="9", padx=40, pady=20, command=lambda: click_btn(9), borderwidth=3)
btn_0 = Button(screen, text="0", padx=40, pady=20, command=lambda: click_btn(0), borderwidth=3)
btn_add = Button(screen, text="+", padx=39, pady=20, command=add_btn, borderwidth=3)
btn_equal = Button(screen, text="=", padx=91, pady=20, command=equal_btn, borderwidth=3)
btn_clear = Button(screen, text="Clear", padx=79, pady=20, command=clear_btn, borderwidth=3)
# Put the buttons on the screen
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_0.grid(row=4, column=0)
btn_add.grid(row=5, column=0)
btn_clear.grid(row=4, column=1, columnspan=2)
btn_equal.grid(row=5, column=1, columnspan=2)
screen.mainloop()

import tkinter
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

win = Tk()
win.geometry("1200x800")
win.option_add("*Font", "맑은고딕 20")
win.config(bg="white")
win.title("ARC")

frame1 = tkinter.Frame(win, relief="solid", bd=2)
frame1.config(width=160, height=600, bg="white")
frame1.grid(column=0, row=0, padx=20, pady=20)

frame2 = tkinter.Frame(win, relief="solid", bd=2)
frame2.config(width=160, height=600, bg="white")
frame2.grid(column=1, row=0, padx=20, pady=20)

frame3 = tkinter.Frame(win, relief="solid", bd=2)
frame3.config(width=160, height=600, bg="white")
frame3.grid(column=2, row=0, padx=20, pady=20)


def start():
    print("실행중입니다")


btn = Button(win)
btn.config(text="실행")
btn.config(command=start)
btn.grid(column=0, row=1)


def f(x):
    y = list()
    for i in x:
        y1 = 1 - np.exp(-i / 10)
        y.append(y1)
    return y


x = [i for i in range(101)]
r = [1 for i in range(101)]
y = f(x)

plt.plot(x, r, '--r', label='input')
plt.plot(x, y, '-b', label='output')
plt.legend(loc='upper right', ncol=1)
plt.axis([0, 100, 0, 1.2])
plt.xlabel('time')
plt.ylabel('response')
plt.title('simulation result')
plt.grid(True, linestyle='--')

fig = Figure(figsize=(10, 7), dpi=100)
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, r, '--r', x, y, '-b')
ax.set_xlim(0, 100)
ax.set_ylim(0, 1.2)
ax.set_xlabel("Time")
ax.set_ylabel("Value")
ax.set_title("Arc Data")
ax.grid(True, linestyle='--')

canvas = FigureCanvasTkAgg(fig, master=win)
canvas.draw()
canvas.get_tk_widget().grid(column=3, row=0)

win.mainloop()

import tkinter
import random

size = 100
color = ["red", "blue", "green", "yellow", "pink"]


# functions
def red_bubble(event=None):
    pad.itemconfig(bubble, fill="red")


def change_bubble_color(event=None):
    pad.itemconfig(bubble, fill=random.choice(color))


# window setup
window = tkinter.Tk()
window.title("Bubble")
window.geometry("600x400")

# Canvas
pad = tkinter.Canvas(window, width="600", height="400", bg="#2a2a2a")
pad.pack()

bubble = pad.create_oval(150 - (size / 2), 150 - (size / 2), 150 + (size /2), 150 + (size / 2), fill="lightgray")
pad.bind_all("w", red_bubble)
pad.bind_all("<space>", change_bubble_color)

window.mainloop()


# 2
import tkinter

size = 20


def Application(event = None):
    key = event.keysym
    if key == "Left":
        pad.move(bubble_1, -10, 0)
    elif key == "Right":
        pad.move(bubble_1, 10, 0)
    elif key == "Up":
        pad.move(bubble_1, 0, -10)
    elif key == "Down":
        pad.move(bubble_1, 0, 10)


# window config
window = tkinter.Tk()
window.title("Bubble")

# canvas
pad = tkinter.Canvas(window, height=300, width=300, bg="#2a2a2a")
pad.pack()

bubble_1 = pad.create_oval((150 - size / 2), 150 - (size / 2), 150 + (size / 2), 150 + (size / 2),
                               fill="lightgray")
pad.bind_all("<Key>", Application)
window.mainloop()


# 3
import tkinter

size = 20


# functions
def stamp(event = None):
    x = event.x
    y = event.y
    pad.create_oval(x - (size / 2), y - (size / 2), x + (size / 2), y + (size / 2), fill="lightgray")


# window setup
window = tkinter.Tk()
window.title("stamp.py")

# canvas setup
pad = tkinter.Canvas(window, height=300, width=300, bg="#2a2a2a")
pad.pack()
pad.bind("<Button-1>", stamp)

window.mainloop()


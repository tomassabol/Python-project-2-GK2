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

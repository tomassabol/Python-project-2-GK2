#1
import tkinter

window = tkinter.Tk()
window.title("Tkinter + Canvas")
window.geometry("600x400")

pad = tkinter.Canvas(window, width="600", height="400", bg="#2a2a2a")
pad.pack()
pad.create_rectangle(10, 10, 100, 200, fill="white", outline="black", width=4)

window.mainloop()



# 2
import tkinter

# window setup
window = tkinter.Tk()
window.title("House")
window.geometry("600x400")

# Canvas
pad = tkinter.Canvas(window, width="600", height="400", bg="lightblue")
pad.pack()
pad.create_rectangle(0, 300, 600, 400, fill="green")  # grass
pad.create_rectangle(100, 180, 240, 300, fill="brown")  # house
pad.create_rectangle(130, 210, 210, 240, fill="white")  # house window
pad.create_polygon(100, 180, 240, 180, 170, 100, fill="red")  # house roof
pad.create_oval(400, 50, 470, 120, fill="yellow", outline="yellow")  # sun

window.mainloop()



# 3
import tkinter

# window setup
window = tkinter.Tk()
window.title("text")
window.geometry("600x400")

# Canvas
pad = tkinter.Canvas(window, width="600", height="400", bg="#2a2a2a")
pad.pack()
for i in range(10):
    pad.create_text(200 + (i * 20), 100 + (i * 20), fill="white", text="Zuzana")


window.mainloop()


# 3 - obloha
import tkinter
import random

# window setup
window = tkinter.Tk()
window.title("Stars")
window.geometry("600x400")


def sky():
    pad.delete("all")

    for i in range(50):
        star_size = random.randint(0, 8) + 2

        x = random.randint(0, 680)
        y = random.randint(0, 380)
        pad.create_oval(x, y, x + star_size, y + star_size, fill="white", outline="white")
    pad.update()


pad = tkinter.Canvas(window, width="600", height="380", bg="#2a2a2a")
pad.pack()

tkinter.Button(window, text="Generate sky", command=sky).pack()

window.mainloop()



# 4 chess
import tkinter


window = tkinter.Tk()
window.title("Chess playground")
window.geometry("640x640")
pad = tkinter.Canvas(window, height=640, width=640, bg="white")
pad.pack()

x = 0
y = 0

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 != 0:
                pad.create_rectangle(x, y, x + 80, y + 80, fill="black")
                x = x + 80
            else:
                x = x + 80
        else:
            if j % 2 == 0:
                pad.create_rectangle(x, y, x + 80, y + 80, fill="black")
                x = x + 80
            else:
                x = x + 80
    x = 0
    y = y + 80

window.mainloop()



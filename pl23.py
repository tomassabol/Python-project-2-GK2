# 1
import tkinter


def number_input():
    if int(input_text.get()) < 0:
        output_text.set(f"{input_text.get()} is lesser than 0")
    elif int(input_text.get()) == 0:
        output_text.set(f"{input_text.get()} is equal to 0")
    else:
        output_text.set(f"{input_text.get()} is greater than 0")


def exit_window():
    window.destroy()


# window setup
window = tkinter.Tk()
window.title("Application")
window.geometry("600x400")

tkinter.Label(window, text="Enter number", bg="white", width=30).pack()
input_text = tkinter.StringVar()
tkinter.Entry(window, textvariable=input_text).pack()

tkinter.Label(window, text="Result", bg="white", width=30).pack()
output_text = tkinter.StringVar()
tkinter.Entry(window, textvariable=output_text).pack()

tkinter.Button(window, text="Get result", bg="white", width=30, command=number_input).pack()
tkinter.Button(window, text="Exit", bg="white", width=30, command=exit_window).pack()

window.mainloop()


# 2
import tkinter


def result_output():
    r = int(number_A.get()) + int(number_B.get())
    result.set(r)


# window config
window = tkinter.Tk()
window.title = "Calculator v1"
window.geometry("600x400")

# number A
tkinter.Label(window, width=30, text="Enter number A: ").grid(row=0, column=0, pady=5)
number_A = tkinter.StringVar()
tkinter.Entry(window, width=10, textvariable=number_A).grid(row=0, column=1, pady=5)

# number B
tkinter.Label(window, width=30, text="Enter number B: ").grid(row=1, column=0, pady=5)
number_B = tkinter.StringVar()
tkinter.Entry(window, width=10, textvariable=number_B).grid(row=1, column=1, pady=5)

# output
tkinter.Button(window, width=10, text="sum up", command=result_output).grid(row=2, column=1, pady=10)
result = tkinter.StringVar()
tkinter.Entry(window, width=10, textvariable=result).grid(row=4, column=1)

window.mainloop()


# 3
import tkinter


def add():
    r = int(number_A.get()) + int(number_B.get())
    result.set(r)


def subtract():
    r = int(number_A.get()) - int(number_B.get())
    result.set(r)


def multiply():
    r = int(number_A.get()) * int(number_B.get())
    result.set(r)


def divide():
    if int(number_B.get()) == 0:
        result.set("ZeroDivisionError")
    else:
        r = int(number_A.get()) / int(number_B.get())
        result.set(r)


# window config
window = tkinter.Tk()
window.title = "Calculator v2"
window.geometry("600x400")

# number A
tkinter.Label(window, width=30, text="Enter number A: ").grid(row=0, column=0, pady=5)
number_A = tkinter.StringVar()
tkinter.Entry(window, width=10, textvariable=number_A).grid(row=0, column=1, pady=5)

# number B
tkinter.Label(window, width=30, text="Enter number B: ").grid(row=1, column=0, pady=5)
number_B = tkinter.StringVar()
tkinter.Entry(window, width=10, textvariable=number_B).grid(row=1, column=1, pady=5)

# functions
tkinter.Button(window, width=25, text="+", command=add).grid(row=2, column=0)
tkinter.Button(window, width=25, text="-", command=subtract).grid(row=2, column=1)
tkinter.Button(window, width=25, text="*", command=multiply).grid(row=3, column=0)
tkinter.Button(window, width=25, text="/", command=divide).grid(row=3, column=1)

# output
result = tkinter.StringVar()
tkinter.Entry(window, width=15, textvariable=result).grid(row=5, column=1)

window.mainloop()


# 4

import tkinter


def application():
    file = open("jazdy.txt", "r")
    data = file.read().split()
    rides = []
    for i in data:
        rides.append(float(i))

    rides_number.set(str(len(rides)))
    total_distance.set(sum(rides))
    avg_length.set(str(sum(rides)/int(len(rides))))
    earned.set(str(round(float(sum(rides)) * float(1.4), 2)))


# window config
window = tkinter.Tk()
window.title("Taxi")
window.geometry("600x400")

# widgets config
# number of rides
tkinter.Label(window, width=30, text="Number or rides:").grid(row=0, column=0)
rides_number = tkinter.StringVar()
tkinter.Entry(window, width=30, textvariable=rides_number).grid(row=0, column=1)

# avg length
tkinter.Label(window, width=30, text="Avg ride length (km):").grid(row=1, column=0)
avg_length = tkinter.StringVar()
tkinter.Entry(window, width=30, textvariable=avg_length).grid(row=1, column=1)

# total distance
tkinter.Label(window, width=30, text="Total distance (km):").grid(row=2, column=0)
total_distance = tkinter.StringVar()
tkinter.Entry(window, width=30, textvariable=total_distance).grid(row=2, column=1)

# Earned
tkinter.Label(window, width=30, text="Earned (€)").grid(row=3, column=0)
earned = tkinter.StringVar()
tkinter.Entry(window, width=30, textvariable=earned).grid(row=3, column=1)

# calc
tkinter.Button(window, width=30, text="Load Data", command=application).grid(row=4, column=1)

window.mainloop()


# 5


import tkinter


def application():
    file = open("shopping.txt", "a")
    file.write(str(item_name.get()) + " " + str(item_price.get()) + "\n")


# window config
window = tkinter.Tk()
window.title("Shopping")
window.geometry("600x400")

# widgets config
# number of rides
tkinter.Label(window, width=30, text="Name of item:").grid(row=0, column=0)
item_name = tkinter.StringVar()
tkinter.Entry(window, width=30, textvariable=item_name).grid(row=0, column=1)

# avg length
tkinter.Label(window, width=30, text="Price (€):").grid(row=1, column=0)
item_price = tkinter.StringVar()
tkinter.Entry(window, width=30, textvariable=item_price).grid(row=1, column=1)

# output
tkinter.Button(window, width=30, text="Save", command=application).grid(row=2, column=1)

window.mainloop()



# 6

import tkinter


def application():
    file_write = open("steps.txt", "a")
    file_read = open("steps.txt", "r")
    data = file_read.read().split()
    s = []
    for i in data:
        s.append(int(i))
    steps_total.set(str(sum(s)))

    file_write.write(str(daily_steps.get()) + "\n")
    daily = int(daily_steps.get())
    total = int(steps_total.get())
    steps_total.set(str(daily + total))


# window config
window = tkinter.Tk()
window.title("Pedometer")
window.geometry("600x400")

# widgets config
# steps today
tkinter.Label(window, width=30, text="Steps Today:").grid(row=0, column=0)
daily_steps = tkinter.StringVar()
tkinter.Entry(window, width=30, textvariable=daily_steps).grid(row=0, column=1)

# steps total
tkinter.Label(window, width=30, text="Total steps:").grid(row=1, column=0)
steps_total = tkinter.StringVar()
tkinter.Entry(window, width=30, textvariable=steps_total).grid(row=1, column=1)

# output
tkinter.Button(window, width=30, text="Save", command=application).grid(row=2, column=1)

window.mainloop()

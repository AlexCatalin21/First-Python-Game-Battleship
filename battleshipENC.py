from tkinter import *


def yourTable():
    a = []
    root = Tk()
    for i in range(6):
        for j in range(6):
            button = Button(root, text="")
            button.grid(column=i)
            button.grid(row=j)
            a.append(button)

    root.mainloop()

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock Using Python")

label = Label(root, font=('aeriel', 24),
              background='white', foreground='black')


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label.pack(anchor='center')
time()

mainloop()

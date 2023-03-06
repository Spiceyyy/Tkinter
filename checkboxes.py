from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

#onvalue="On", offvalue="Off"
var = StringVar()
c = Checkbutton(root, text="Check this box, I dare you", variable=var,onvalue="On", offvalue="Off")
c.deselect()
c.pack()

my_btn = Button(root, text="Show selection", command=show).pack()

root.mainloop()
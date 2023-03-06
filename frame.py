from tkinter import *
from PIL import ImageTk, Image

root = Tk()

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=100, pady=100)

b = Button(frame, text="Don't Click Here")
b.grid(row=0, column=0)

b = Button(frame, text=" Or Don't Click Here")
b.grid(row=1, column=1)

root.mainloop()
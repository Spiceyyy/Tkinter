from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text='Look! I clicked a Button')
    myLabel.pack()

myButton = Button(root, text='Click me!', command=myClick, fg="blue")
# state=DISABLED to gray out the button
# padx to make it bigger on x axis
# pady to make it bigger on y axis
# command=(function name) to create a command for a button
# fg="colour" to change colour of letters (hex colour codes works too)
# bg="colour" to change colour of the background (hex colour codes works too)
myButton.pack()

root.mainloop()
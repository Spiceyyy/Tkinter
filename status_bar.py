from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image output')
#root.iconbitmap('path of the icon (.ico)')

my_img1 = ImageTk.PhotoImage(Image.open('images/asd.png'))
my_img2 = ImageTk.PhotoImage(Image.open('images/alley.png'))
my_img3 = ImageTk.PhotoImage(Image.open('images/boba.png'))

image_list = [my_img1, my_img2, my_img3]

status = Label(root, text='Image 1 of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number+1))
    button_back = Button(root, text='<<', command=lambda: back(image_number-1))
    if image_number == len(image_list):
        button_forward = Button(root,text=">>", state=DISABLED)

    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    my_label.grid(row=0,column=0, columnspan=3)

    status = Label(root, text='Image '+ str(image_number) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number+1))
    button_back = Button(root, text='<<', command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text='<<', state=DISABLED)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    my_label.grid(row=0,column=0, columnspan=3)

    status = Label(root, text='Image '+ str(image_number) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='Exit Program', command=root.quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
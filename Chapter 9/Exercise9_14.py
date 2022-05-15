from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT

def move(dx, dy):
    global x, y, canvas
    canvas.create_line(x, y, x + dx, y + dy)
    x += dx
    y += dy

root = Tk()

# canvas with border of size 100 x 150
canvas = Canvas(root, height=100, width=150,
                relief=SUNKEN, borderwidth=3)
canvas.pack(side=LEFT)

# frame to hold the 4 buttons
box = Frame(root)
box.pack(side=RIGHT)

# the 4 button widgets have Frame widget box as their master
button = Button(box, text='up', command=lambda: move(0, -10))
button.grid(row=0, column=0, columnspan=2)
button = Button(box, text='left',command=lambda: move(-10, 0))
button.grid(row=1, column=0)
button = Button(box, text='right', command=lambda: move(10, 0))
button.grid(row=1, column=1)
button = Button(box, text='down', command=lambda: move(0, 10))
button.grid(row=2, column=0, columnspan=2)

x, y = 50, 75 # pen position, initially in the middle




root.mainloop()


from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT



# event handlers
def up():
    'move pen up 10 pixels'
    global y, canvas                  # y is modified
    canvas.create_line(x, y, x, y-10)
    y -= 10

def down():
    'move pen down 10 pixels'
    global y, canvas                  # y is modified
    canvas.create_line(x, y, x, y+10)
    y += 10

def left():
    'move pen left 10 pixels'
    global x, canvas                  # x is modified
    canvas.create_line(x, y, x-10, y)
    x -= 10

def right():
    'move pen right 10 pixels'
    global x, canvas                  # x is modified
    canvas.create_line(x, y, x+10, y)
    x += 10



root = Tk()

# canvas with border of size 100 x 150
canvas = Canvas(root, height=100, width=150,
                relief=SUNKEN, borderwidth=3)
canvas.pack(side=LEFT)

# frame to hold the 4 buttons
box = Frame(root)
box.pack(side=RIGHT)

# the 4 button widgets have Frame widget box as their master
button = Button(box, text='up', command=up)
button.grid(row=0, column=0, columnspan=2)
button = Button(box, text='left',command=left)
button.grid(row=1, column=0)
button = Button(box, text='right', command=right)
button.grid(row=1, column=1)
button = Button(box, text='down', command=down)
button.grid(row=2, column=0, columnspan=2)

x, y = 50, 75 # pen position, initially in the middle


root.mainloop()


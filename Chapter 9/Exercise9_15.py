from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT

lastx = 0
lasty = 0
identity = 0

# event handlers
def up():
    'move pen up 10 pixels'
    global identity, y, canvas, lasty, lastx                  # y is modified
    identity += 1
    canvas.create_line(x, y, x, y-10, tags='last'+str(identity))
    y -= 10
    lasty = 10
    lastx = 0

def down():
    'move pen down 10 pixels'
    global identity, y, canvas, lasty, lastx                  # y is modified
    identity += 1
    canvas.create_line(x, y, x, y+10, tags='last'+str(identity))
    y += 10
    lastx = 0
    lasty = -10

def left():
    'move pen left 10 pixels'
    global identity, x, canvas, lastx, lasty                  # x is modified
    identity += 1
    canvas.create_line(x, y, x-10, y, tags='last'+str(identity))
    x -= 10
    lasty = 0
    lastx = 10

def right():
    'move pen right 10 pixels'
    global identity, x, canvas, lastx, lasty                  # x is modified
    identity += 1
    canvas.create_line(x, y, x+10, y, tags='last'+str(identity))
    x += 10
    lasty = 0
    lastx = -10

def clear():
    global canvas
    canvas.addtag_all(all)
    canvas.delete(all)


def delete():
    global identity, canvas, x, y, lastx, lasty
    canvas.delete('last'+str(identity))
    x += lastx
    y += lasty

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
button = Button(box, text='clear', command=clear)
button.grid(row=3, column=0)
button = Button(box, text='delete', command=delete)
button.grid(row=3, column=1)

x, y = 50, 75 # pen position, initially in the middle


root.mainloop()


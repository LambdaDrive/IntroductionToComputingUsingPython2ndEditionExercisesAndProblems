from tkinter import Tk, Canvas


def begin(event):
    'initializes the start of the curve to mouse position'

    global oldx, oldy
    oldx, oldy = event.x, event.y


def draw(event):
    'draws a line segment from old mouse position to new one'
    global oldx, oldy, canvas      # x and y will be modified
    newx, newy = event.x, event.y  # new mouse position

    # connect previous mouse position to current one
    canvas.create_line(oldx, oldy, newx, newy)
    
    oldx, oldy = newx, newy    # new position becomes previous



root = Tk()

oldx, oldy = 0, 0   # mouse coordinates (global variables)

# canvas
canvas = Canvas(root, height=100, width=150)

# bind left mouse button click event to function begin() 
canvas.bind("<Button-1>", begin)

# bind mouse motion while pressing left button event 
canvas.bind("<Button1-Motion>", draw)

canvas.pack()

root.mainloop()

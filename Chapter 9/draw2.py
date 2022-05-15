from tkinter import Tk, Canvas

def begin(event):
    'initializes the start of the curve to mouse position'
    global oldx, oldy, curve
    oldx, oldy = event.x, event.y
    curve = []

def draw(event):
    'draws a line segment from old mouse position to new one'
    global oldx, oldy, canvas, curve  # x and y will be modified
    newx, newy = event.x, event.y     # new mouse position

    # connect previous mouse position to current one
    curve.append(canvas.create_line(oldx, oldy, newx, newy))
    
    oldx, oldy = newx, newy            # new position becomes previous

def delete(event):
    'delete last curve drawn'
    global curve
    for segment in curve:
        canvas.delete(segment)                 

root = Tk()

oldx, oldy = 0, 0   # mouse coordinates (global variables)

# canvas
canvas = Canvas(root, height=100, width=150)

# bind left mouse button click event to begin() 
canvas.bind("<Button-1>", begin)

# bind mouse motion while pressing left button event to draw()
canvas.bind("<Button1-Motion>", draw)

# bind Ctrl-Left button mouse click to delete()
canvas.bind('<Control-Button-1>', delete)

canvas.pack()
root.mainloop()

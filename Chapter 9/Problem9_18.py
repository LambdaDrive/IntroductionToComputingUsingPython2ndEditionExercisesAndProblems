#9.18 Develop a GUI that contains just one Frame widget of size 480 × 640 that has this
#behavior: Every time the user clicks at some location in the frame, the location coordinates
#are printed in the interactive shell.
#>>>
#you clicked at (55, 227)
#you clicked at (426, 600)
#you clicked at (416, 208)

def click(event):
    print('you clicked at ({},{})'.format(event.x, event.y))

from tkinter import *

root = Tk()

frame = Frame(root, height = 480, width = 640)
frame.pack()
frame.bind('<Button>', click)

root.mainloop()

from tkinter import *

def imprint(text):
    global entrynumber

    entrynumber.insert(len(entrynumber.get()), text)

    if len(entrynumber.get()) == 3:
        entrynumber.insert(3, '-')
    elif len(entrynumber.get()) == 7:
        entrynumber.insert(7, '-')

root = Tk()

framedisplay = Frame(root)
framedisplay.pack(side=TOP)
framedigits = Frame(root)
framedigits.pack(side=BOTTOM)

entrynumber = Entry(framedisplay)
entrynumber.pack()

labels = [['1', '2', '3'],     # phone dial label texts
          ['4', '5', '6'],     # organized in a grid
          ['7', '8', '9'],
          ['*', '0', '#']]


for r in range(4):      # for every row r = 0, 1, 2, 3
    for c in range(3):      # for every row c = 0, 1, 2
        # create label for row r and column c
        button = Button(framedigits,
                      relief=RAISED,      # raised border
                      padx=10,            # make label wide
                      text=labels[r][c],  # label text  
                      command=lambda text=labels[r][c]:imprint(text))
        
        # place label in row r and column c
        button.grid(row=r, column=c)

root.mainloop()

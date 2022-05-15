from tkinter import *
import random

def rolla():

    dice = (random.randrange(1,7))+(random.randrange(1,7))
    
    return dice

def newgame():

    global entry, buttonroll

    roll = rolla()
    entry.delete(0, 3)
    entry.insert(0, roll)
    if roll!=7 and roll!=11 and roll!=2 and roll!=3 and roll!=12:
        buttonroll.config(state=NORMAL)

def rollforpoint():
    global entry, buttonroll
    roll = rolla()
    entry.delete(0, 3)
    entry.insert(0, roll)
    if roll==7 or roll==11 or roll==2 or roll==3 or roll==12:
        buttonroll.config(state=DISABLED)

root = Tk()

label = Label(root, text='Your roll:')
label.grid(row=0, column=0, columnspan=2)

entry = Entry(root)
entry.grid(row=1, column=0, columnspan=2)

buttongame = Button(root, text='New game', command=newgame)
buttongame.grid(row=2, column=0)

buttonroll = Button(root, text='Roll for point', state = DISABLED, command=rollforpoint)
buttonroll.grid(row=2, column=1)

root.mainloop()

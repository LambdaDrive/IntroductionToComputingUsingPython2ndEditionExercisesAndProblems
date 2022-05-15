from tkinter import *
from tkinter.messagebox import showinfo
import random

correct = random.randint(0, 9)

def guess(event):
    global entry, correct
    if int(entry.get()) == correct:
        showinfo(message='The guess is correct')
        

root = Tk()

label = Label(root, text = 'Enter your guess:')
label.grid(row = 0, column = 0)

entry = Entry(root)
entry.grid(row = 1, column = 0)

button = Button(root, text = 'Enter', command = guess)
button.grid(row = 2, column = 0)

root.bind('<Return>', guess)

root.mainloop()

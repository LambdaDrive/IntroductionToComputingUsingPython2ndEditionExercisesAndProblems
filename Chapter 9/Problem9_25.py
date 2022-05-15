from tkinter import *
from tkinter.messagebox import showinfo
import random

a = random.randint(1, 9)
b = random.randint(1, 9)
choiceoperation = random.randrange(0, 2)
print(choiceoperation)
if choiceoperation == 0:
    operation = '+'
    result = a + b
else:
    operation = '-'
    if a > b:
        result = a - b
    else:
        result = b - a

if a > b:
    expression = '{} {} {}'.format(a, operation, b)
else:
    expression = '{} {} {}'.format(b, operation, a)

def getresult(event=0):
    global entryresult, result
    if int(entryresult.get()) == result:
        showinfo(message = 'You got it!')

    


root = Tk()

entrycalculate = Entry(root)
entrycalculate.grid(row = 0, column = 0)
entrycalculate.insert(1, expression)

entryresult = Entry(root)
entryresult.grid(row = 1, column = 0)

button = Button(root, text = 'Enter', command = getresult)
button.grid(row = 2, column = 0)

root.bind('<KeyPress-Return>' ,getresult)

root.mainloop()

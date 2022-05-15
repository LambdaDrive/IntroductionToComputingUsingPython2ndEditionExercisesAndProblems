from tkinter import *
from tkinter.messagebox import showinfo
import random

tries = 0
result = 0
def generateproblem():
    global result
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    choiceoperation = random.randrange(0, 2)
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

    return expression

expression = generateproblem()

def getresult(event=0):
    global entryresult, result, expression, tries, entrycalculate
    if int(entryresult.get()) == result:
        showinfo(message = 'Number of tries = {} \n You got it!'.format(tries))
        expression = generateproblem()
        entrycalculate.delete(0, 10)
        entrycalculate.insert(1, expression)
        tries = 0
    else:
        tries += 1

    


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

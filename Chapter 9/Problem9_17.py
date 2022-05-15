from tkinter import *

def calculatemortgage():
    global entryloan, entryinterest, entryterm, entrymortgage
    a = float(entryloan.get())
    r = float(entryinterest.get())
    t = float(entryterm.get())
    c = r/1200
    m = a*c*((1 + c)**t)/((1 + c)**t) -1
    entrymortgage.delete(0, 10)
    entrymortgage.insert(1, str(m))


root = Tk()

frameentry = Frame(root)
frameentry.grid(row = 0)
framebutton = Frame(root)
framebutton.grid(row=1)

labelloan = Label(frameentry, text='Loan amount:')
labelloan.grid(row = 0, column = 0)
entryloan = Entry(frameentry)
entryloan.grid(row = 0, column = 1)
labelinterest = Label(frameentry, text = 'Interest Rate:')
labelinterest.grid(row = 1, column = 0)
entryinterest = Entry(frameentry)
entryinterest.grid(row = 1, column = 1)
labelterm = Label(frameentry, text = 'Loan term:')
labelterm.grid(row = 2, column = 0)
entryterm = Entry(frameentry)
entryterm.grid(row = 2, column = 1)
labelmortgage = Label(frameentry, text = 'Mortgage')
labelmortgage.grid(row = 3, column = 0)
entrymortgage = Entry(frameentry)
entrymortgage.grid(row = 3, column = 1)

buttonmortgage = Button(framebutton, text = 'Compute Mortgage', command = calculatemortgage)
buttonmortgage.pack()

from tkinter import *
from tkinter.messagebox import showinfo

def bmi():
    global height, weight
    
    altura = float(height.get())
    peso = float(weight.get())
    height.delete(0, 4)
    weight.delete(0, 4)
    bmi = peso/altura**2
    message = 'Your BMI is:{}'.format(bmi)
    showinfo(message=message)



root = Tk()

frameup = Frame(root)
frameup.grid(row=0)

framebutton = Frame(root)
framebutton.grid(row=1)

labelheight = Label(frameup, text = 'Enter your height:')
labelheight.grid(row=0, column=0)
height = Entry(frameup)
height.grid(row=0, column = 1)
labelweight = Label(frameup, text = 'Enter your weight:')
labelweight.grid(row = 1, column = 0)
weight = Entry(frameup)
weight.grid(row = 1, column = 1)

buttoncompute = Button(framebutton, text = 'Compute BMI', command=bmi)
buttoncompute.pack()

root.mainloop()

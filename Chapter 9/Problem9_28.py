from tkinter import *
from tkinter.simpledialog import askstring
import time
from calendar import monthrange
from math import ceil

class Calendar:

    apointment = ''

    def __init__(self, master, year, month):
        firstdaydays = monthrange(year, month)
        monthday = 1
        rows = ceil((firstdaydays[1]/7)+1)
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']
        apoint = dict()

        for i in range(1, firstdaydays[1]):
            apoint[i] = ''

        def apointment(day):
            if apoint[day] == '':
                apoint[day] = askstring('example', 'Enter text')
            else:
                apoint[day] = askstring('example', 'Enter text', initialvalue=apoint[day])
                

        

        for i in range(len(days)):
            label = Label(master, text=days[i])
            label.grid(row = 0, column = i)

        
        
        for i in range(1, rows):
            if i == 1:
                for a in range(firstdaydays[0], 7):
                    button = Button(root, text=monthday, command=lambda text=monthday:apointment(text))
                    button.grid(row = i, column = a)
                    monthday += 1
            else:
                for a in range(7):
                    button = Button(root, text=monthday, command=lambda text=monthday:apointment(text))
        
                    button.grid(row = i, column = a)
                    monthday +=1
                    if monthday == firstdaydays[1] + 1:
                        monthday = 0
                        break

        master.mainloop()

                    
        
        

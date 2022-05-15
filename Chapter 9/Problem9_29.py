from tkinter import *
from tkinter.simpledialog import askstring
import time
from calendar import monthrange
from math import ceil
import datetime

class Calendar:

    apointment = ''
    
    def __init__(self, master):
        self.month = datetime.date.today().month
        self.year = datetime.date.today().year
        apoint = dict()
        apointmont = dict()
        apointyear = dict()
        

        def generatemonth(month, year):
            for widget in master.winfo_children():
                widget.destroy()
            firstdaydays = monthrange(year, month)
            monthday = 1
            rows = ceil((firstdaydays[1]/7)+2)
            days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']

            for i in range(1, firstdaydays[1]):
                apoint[i] = ''

            apointmont[month] = apoint
            apointyear[year] = apointmont

            backward = Button(master, text = 'Previous', command = backwards)
            backward.grid(row=0, column = 0)

            yearmonth = Label(master, text = '{}, {}'.format(self.month, self.year))
            yearmonth.grid(row = 0, column = 1)

            nexto = Button(master, text = 'next', command=forward)
            nexto.grid(row = 0, column = 2)

            for i in range(len(days)):
                label = Label(master, text=days[i])
                label.grid(row = 1, column = i)


            for i in range(2, rows):
                if i == 2:
                    for a in range(firstdaydays[0], 7):
                        button = Button(root, text=monthday, command=lambda text=[year, month, monthday]:apointment(text))
                        button.grid(row = i, column = a)
                        monthday += 1
                else:
                    for a in range(7):
                        button = Button(root, text=monthday, command=lambda text=[year, month, monthday]:apointment(text))
                        button.grid(row = i, column = a)
                        monthday +=1

                        if monthday == firstdaydays[1] + 1:
                            monthday = 0
                            break


        
        
        def apointment(day):
            if apointyear[day[0]][day[1]][day[2]] == '':
                apointyear[day[0]][day[1]][day[2]] = askstring('example', 'Enter text')
            else:
                apointyear[day[0]][day[1]][day[2]] = askstring('example', 'Enter text', initialvalue=apointyear[day[0]][day[1]][day[2]])
                

        def backwards():
            if self.month == 1:
                self.month = 12
                self.year -= 1
            else:
                self.month -= 1
            generatemonth(self.month, self.year)

        def forward():
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
            generatemonth(self.month, self.year)
            
        generatemonth(self.month, self.year)

        master.mainloop()

                    
        
        

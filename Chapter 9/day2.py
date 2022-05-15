from tkinter import Tk, Button, Entry, Label, END
from time import strptime, strftime
from tkinter.messagebox import showinfo



def compute():
    '''display day of the week corresponding to date in dateEnt;
       date must have the format MMM DD, YYY (e.g. Jan 21, 1967)'''


    global dateEnt   # dateEnt is a global variable

    # read date from entry dateEnt
    date = dateEnt.get()

    # compute weekday corresponding to date
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))

    # display the weekday in a pop-up window  
    dateEnt.insert(0, weekday + ' ')



def clear():
    'clears entry datEnt'
    global dateEnt
    dateEnt.delete(0, END)
    


root = Tk()

# label
label = Label(root, text='Enter date')
label.grid(row=0, column=0)

# entry
dateEnt = Entry(root)
dateEnt.grid(row=0, column=1)

# Enter button
button = Button(root, text='Enter', command=compute) 
button.grid(row=1, column=0)

# Clear button
button = Button(root, text='Clear', command=clear) 
button.grid(row=1, column=1)

root.mainloop()

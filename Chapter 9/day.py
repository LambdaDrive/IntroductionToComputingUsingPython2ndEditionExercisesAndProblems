from tkinter import Tk, Button, Entry, Label, END
from time import strptime, strftime
from tkinter.messagebox import showinfo

def compute():
    '''display day of the week corresponding to date in dateEnt;
       date must have format MMM DD, YYYY (e.g., Jan 21, 1967)'''

    global dateEnt   # dateEnt is a global variable

    # read date from entry dateEnt
    date = dateEnt.get()

    # compute weekday corresponding to date
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))

    # display the weekday in a pop-up window  
    showinfo(message = '{} was a {}'.format(date, weekday))

    # delete date from entry dateEnt
    dateEnt.delete(0, END)



root = Tk()

# label
label = Label(root, text='Enter date')
label.grid(row=0, column=0)

# entry
dateEnt = Entry(root)
dateEnt.grid(row=0, column=1)

# Solution to Practice Problem 9.5
# def compute2(event):
#   compute()
# dateEnt.bind('<Return>', compute2)

# button
button = Button(root, text='Enter', command=compute) 
button.grid(row=1, column=0, columnspan=2)

root.mainloop()

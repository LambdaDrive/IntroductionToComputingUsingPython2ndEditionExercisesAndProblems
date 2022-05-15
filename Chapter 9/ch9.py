from tkinter import Button, Frame
from tkinter.messagebox import showinfo
from time import strftime, localtime

class ClickIt(Frame):
    'GUI that shows current time'

    def __init__(self, master=None):
        'constructor'
        Frame.__init__(self, master)
        self.pack()
        button = Button(self,
                        text='Click it',
                        command=self.clicked)
        button.pack()

    def clicked(self):
        'prints day and time info'
        time = strftime('Day:  %d %b %Y\nTime: %H:%M:%S %p\n',
                        localtime())
        showinfo(message=time)



from tkinter import Tk, Button, Entry, Label, END
from time import strptime, strftime
from tkinter.messagebox import showinfo

class Day(Frame):
    'an application that computes weekday corresponding to a date'
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        
        # label
        label = Label(self, text='Enter date')
        label.grid(row=0, column=0)

        # entry
        self.dateEnt = Entry(self)             # instance variable
        self.dateEnt.grid(row=0, column=1)

        # button
        button = Button(self, text='Enter', command=self.compute) 
        button.grid(row=1, column=0, columnspan=2)
        

    def compute(self):
        '''display weekday corresponding to date in dateEnt; date
           must have format MMM DD, YYYY (e.g., Jan 21, 1967)'''


        # read date from entry dateEnt
        date = self.dateEnt.get()

        # compute weekday corresponding to date
        weekday = strftime('%A', strptime(date, '%b %d, %Y'))

        # display the weekday in a pop-up window  
        showinfo(message = '{} was a {}'.format(date, weekday))

        # delete date from entry dateEnt
        self.dateEnt.delete(0, END)



from tkinter import Canvas, Frame, BOTH
class Draw(Frame):
    'a basic drawing application'

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()

        # mouse coordinates are instance variables
        self.oldx, self.oldy = 0, 0

        # create canvas and bind mouse events to handlers
        self.canvas = Canvas(self, height=100, width=150)
        self.canvas.bind("<Button-1>", self.begin)
        self.canvas.bind("<Button1-Motion>", self.draw)
        self.canvas.pack(expand=True, fill=BOTH)

    def begin(self, event):
        'handles left button click by recording mouse position'
        self.oldx, self.oldy = event.x, event.y
        
    def draw(self, event):
        '''handles mouse motion, while pressing left button, by
           connecting the previous mouse position to the new one'''
        newx, newy = event.x, event.y
        self.canvas.create_line(self.oldx, self.oldy, newx, newy)
        self.oldx, self.oldy = newx, newy



##################################
# Solutions to Practice Problems #
##################################



# Practice Problem 9.2
from tkinter import Tk, Label
from calendar import monthrange

def cal(year, month):
    'display a window with the calendar for the given month and year'

    root = Tk()

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # create and place weekday labels
    for i in range(7):
        label = Label(root, text=days[i])
        label.grid(row=0, column=i)

    # obtain the day of the week for first of the month and
    # the number of days in the month
    weekday, numDays = monthrange(year, month)
    # create calendar starting with week (row) 1 and day (column) 1
    week = 1
    for i in range(1, numDays+1): # for i = 1, 2, ..., numDays
        # create label i and place it in row week, column weekday
        label = Label(root, text=str(i))
        label.grid(row=week, column=weekday)

        # update weekday (column) and week (row)
        weekday += 1
        if weekday > 6:
            week += 1
            weekday = 0

    root.mainloop()



# Practice Problem 9.8
from tkinter import Text, Frame, BOTH
class KeyLogger(Frame):
    'a basic editor that logs key strokes'
    
    def __init__(self, master=None):
        'creates Text widget and binds key strokes to handler record'
        Frame.__init__(self, master)
        self.pack()
        text = Text(width=20, height=5)
        text.bind('<KeyPress>', self.record)
        text.pack(expand=True, fill=BOTH)
        
    def record(self, event):
        '''handles key stroke events by printing character
           associated with key'''
        print('char={}'.format(event.keysym))



from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT
class Plotter(Frame):
    'a simple pen drawing app'
    
    def __init__(self, parent=None):
        'arrange canvas and 4 button widgets controling the pen'
        Frame.__init__(self, parent)
        self.pack()

        self.x = 75                # x-coordinate of pen
        self.y = 50                # y-coordinate of pen

        self.canvas = Canvas(self, height=100, width=150,
                             relief=SUNKEN, borderwidth=3)
        self.canvas.pack(side=LEFT)

        buttons = Frame(self)
        buttons.pack(side=RIGHT)

        # create up button
        b = Button(buttons, text='up', command=self.up)
        b.grid(row=0, column=0, columnspan=2)
        
        # create left button
        b = Button(buttons, text='left', command=self.left)
        b.grid(row=1, column=0)
        
        # create right button
        b = Button(buttons, text='right', command=self.right)
        b.grid(row=1, column=1)
        
        # create down button
        b = Button(buttons, text='down', command=self.down)
        b.grid(row=2, column=0, columnspan=2)


    def up(self):
        'move pen up 10 pixels'
        self.canvas.create_line(self.x, self.y, self.x, self.y-10)
        self.y -= 10

    def down(self):
        'move pen down 10 pixels'
        self.canvas.create_line(self.x, self.y, self.x, self.y+10)
        self.y += 10

    def left(self):
        'move pen left 10 pixels'
        self.canvas.create_line(self.x, self.y, self.x-10, self.y)
        self.x -= 10

    def right(self):
        'move pen right 10 pixels'
        self.canvas.create_line(self.x, self.y, self.x+10, self.y)
        self.x += 10


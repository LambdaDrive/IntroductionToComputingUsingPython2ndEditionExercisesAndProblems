from tkinter import Tk, Button, LEFT, RIGHT
from time import strftime, localtime, gmtime

def greenwich():
    'prints Greenwich day and time info'
    time = strftime('Day:  %d %b %Y\nTime: %H:%M:%S %p\n',
                    gmtime())
    print('Greenwich time\n' + time)

def local():
    'prints local day and time info'
    time = strftime('Day:  %d %b %Y\nTime: %H:%M:%S %p\n',
                    localtime())
    showinfo('Local time\n' + time)

root = Tk()

# Local time button
buttonl = Button(root,
                 text='Local time',
                 command=local)

# Greenwich mean time button
buttong = Button(root,
                 text='Greenwich time',
                 command=greenwich)

buttonl.pack(side = LEFT)
buttong.pack(side = RIGHT)
root.mainloop()

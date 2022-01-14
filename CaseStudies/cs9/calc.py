from tkinter import Tk, Button, Frame, Entry, END, RIDGE, RAISED
from math import sqrt

class Calc(Frame):
    'a simple calculator'

    def __init__(self, parent=None):
        'calculator constructor'
        Frame.__init__(self, parent)
        self.pack()

        self.memory = ''                     # memory storage
        self.expr = ''                       # current expression storage
        self.startOfNextOperand = True       # start of new operand 

        # use Entry widget for display
        self.entry = Entry(self, relief=RIDGE, borderwidth=3,
                           width=20, bg='gray',
                           font=('Helvetica', 18))
        self.entry.grid(row=0, column=0, columnspan=5)

        # calculator button labels in a 2D list
        buttons = [['MC',     'M+',      'M-', 'MR'],
                   ['C' , '\u221a', 'x\u00b2', '+' ],
                   ['7' ,     '8' ,      '9' , '-' ],
                   ['4' ,     '5' ,      '6' , '*' ],
                   ['1' ,     '2' ,      '3' , '/' ],
                   ['0' ,     '.' ,      '+-', '=' ]]
               
        # create and place buttons in appropriate row and column
        for r in range(6):
            for c in range(4):

                # function cmd() is defined so that when it is
                # called without an input argument, it executes
                # self.click(buttons[r][c])
                def cmd(x=buttons[r][c]):
                    self.click(x)

                b = Button(self,       # button for symbol buttons[r][c]
                           text=buttons[r][c],
                           width=3,
                           relief=RAISED,
                           command=cmd)          # cmd() is the handler
                b.grid(row=r+1, column=c)        # entry is in row 0

        
    def click(self, key):
        'handler for event of pressing button labeled key'

        if key == '=':
            # evaluate the expression, including the value
            # displayed in entry and display result
            try:
                result = eval(self.expr + self.entry.get())
                self.entry.delete(0, END)
                self.entry.insert(END, result)
                self.expr = ''
            except:
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error')
                
        elif key in '+*-/':
            # add operand displayed in entry and operator key
            # to expression and prepare for next operand
            self.expr += self.entry.get()
            self.expr += key
            self.startOfNextOperand = True
            
        elif key == '\u221a':
            # compute and display square root of entry
            result = sqrt(eval(self.entry.get()))
            self.entry.delete(0, END)
            self.entry.insert(END, result)
            
        elif key == 'x\u00b2':
            # compute and display the square of entry
            result = eval(self.entry.get())**2
            self.entry.delete(0, END)
            self.entry.insert(END, result)
            
        elif key == 'C':
            # clear entry
            self.entry.delete(0, END)
            
        elif key in {'M+', 'M-'}:
            # add or subtract entry value from memory
            self.memory = str(eval(self.memory + key[1] + self.entry.get()))

        elif key == 'MR':
            # replace value in entry with value stored in memory
            self.entry.delete(0, END)
            self.entry.insert(END, self.memory)

        elif key == 'MC':
            # clear memory
            self.memory = ''

        elif key == '+-':
            # switch entry from positive to negative or vice versa
            # if there is no value in entry, do nothing
            try:
                if self.entry.get()[0] == '-':
                    self.entry.delete(0)
                else:
                    self.entry.insert(0, '-')
            except IndexError:
                pass

        else:
            # insert digit at end of entry, or as the first
            # digit if start of next operand
            if self.startOfNextOperand:
                self.entry.delete(0, END)
                self.startOfNextOperand = False
            self.entry.insert(END, key)


if __name__ == '__main__':
   root = Tk()
   calc = Calc(root)
   root.mainloop()

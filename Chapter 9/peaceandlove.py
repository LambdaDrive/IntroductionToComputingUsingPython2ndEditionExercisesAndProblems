from tkinter import Tk, Label, PhotoImage, BOTH, RIGHT, LEFT
root = Tk()

label1 = Label(root, text='Peace & Love', background='black',
               width=20, height=5, foreground='white',
               font=('Helvetica', 18, 'italic'))
label1.pack(side=LEFT)

photo = PhotoImage(file='peace.gif')
label2 = Label(root, image=photo)
label2.pack(side=RIGHT, expand=True, fill=BOTH)

root.mainloop()

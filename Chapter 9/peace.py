from tkinter import Tk, Label, PhotoImage
root = Tk()                  # the window
# transform GIF image to a format tkinter can display     
photo = PhotoImage(file='peace.gif')

peace = Label(master=root,
              image=photo,
              width=300,   # width of label, in pixels
              height=180)  # heigh of label, in pixels
peace.pack()
root.mainloop()

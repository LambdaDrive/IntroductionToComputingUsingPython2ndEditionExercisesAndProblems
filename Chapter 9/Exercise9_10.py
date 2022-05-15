from tkinter import Tk, PhotoImage, Label, RIGHT, LEFT

root = Tk()
picture = PhotoImage(file='Rotating_earth_(large).gif')
imagem = Label(master=root,image=picture)
imagem.pack(side=RIGHT)
text = Label(text='Terra \n 23487283742830947 anos')
text.pack(side=LEFT)

root.mainloop()

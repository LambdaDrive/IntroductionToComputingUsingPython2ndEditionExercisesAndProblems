from tkinter import Tk, Text, BOTH

def record(event):
    '''event handling function for key press event;
       input event is of type tkinter.Event'''
    print('char = {}'.format(event.keysym)) # print key symbol

root = Tk()

text = Text(root,
            width=20,  # set width to 20 characters
            height=5)  # set height to 5 rows of characters

# Bind a key press event with the event handling function record()
text.bind('<KeyPress>', record)

# widget expands if the master does
text.pack(expand=True, fill=BOTH)

root.mainloop()

from tkinter import *
import time

times = [[]]
numbword = 0
timeword = 0
timetotal = []

def timedigit(event):
    global times, numbword, timeword, timetotal
    if event.keysym != "space":
        times[numbword].append(time.time())
    else:
        times[numbword].append(time.time())
        times.append([])
        for a in range((len(times[numbword]))-1):
            timeword += (times[numbword][a+1]) - (times[numbword][a])
        timetotal.append(timeword)
        print("Last word time(sec):{} \n Words per minute:{}".format(int(timeword), int(60/((sum(timetotal)/len(timetotal))))))
        numbword += 1
        timeword = 0    
                
                




root = Tk()

textbox = Text(root, height = 10, width = 20)
textbox.pack()

textbox.bind('<KeyPress>', timedigit)

root.mainloop()

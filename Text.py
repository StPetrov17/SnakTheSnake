from tkinter import *
import time


#defining TK()
root = Tk()


#defining Functions

def timesnow():
    currentime = time.strftime ("%H:%M:%S")
    timelabel.config (text=currentime)

    timelabel.after(1000, timesnow)


#creatng GUI's
timelabel = Label(root, font=("Courier", 44))
timelabel.grid()
timesnow()


input = Entry(root)
input.grid()

setbutton = Button(text = "Set Your ALARM")
setbutton.grid()


root.mainloop()
#Import the required libraries
from veriables import *
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry of Tkinter Frame
win.geometry(f"{GAME_HEIGHT}x{GAME_WIDTH}")

#Define a function for exit
def exit_program():
   win.destroy()

#Add a canvas widget
canvas = Canvas(win, bg=BACKGROUND_COLOR, height=1000, width=1000)

#Add a Label widget in the Canvas
label = Label(canvas, text= "Click the Button to Exit", font= ('Helvetica 17 bold'))
label.pack(pady= 30)

#Create a button in canvas widget
ttk.Button(canvas, text= "Exit", command= exit_program).pack()
canvas.pack()

win.mainloop()
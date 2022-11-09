from tkinter import *

color = 1

root = Tk()

def myClick():
    global color
    if color == 1:
        color = 0
        myLabel = Label(root,text="Look! You clicked a button!", fg = "green", bg = "red",padx=500,font=("Arial",20))
        myLabel.pack()
    elif color == 0:
        color = 1
        myLabel = Label(root,text="Look! You clicked a button!", fg = "red", bg = "green",padx=500,font=("Arial",20))
        myLabel.pack()

myButton = Button(root, text="Click Me",padx = 500,pady=15,command=myClick, fg = "green", bg = "red",font=("Arial",35))

myButton.pack()


root.mainloop()
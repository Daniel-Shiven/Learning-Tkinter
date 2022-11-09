#----- TO DO LIST -----#
#
# -Add the ability to make decimal points
# -Add exponents
# -Add logarithims
# -Add Trig
# -Add Degrees vs Radians button
# -Make it into an exe file


from tkinter import *
import tkinter.font as font


#---Establishing the Window---#
root = Tk()
root.title("Epic Calculator")

#---Creating entry box---#
e = Entry(root, width=29, borderwidth=5,font=25)
e.grid(row=0,column=0,columnspan=3, ipady=10,pady=10,padx=2)

global times
times = 0

global entries
entries = 0

def button_click(number):
    global times
    times = times+1

    if times == 1:
        global resultado
        resultado = 0

    if resultado == 1:
        resultado = 0
        e.delete(0, END)

    past = e.get()
    e.delete(0, END)
    e.insert(0, str(past) + str(number))

def clear():
    global entries
    entries = 0
    e.delete(0,END)

def pemdas(type):
    global num_1
    global num_2
    global operation
    global entries
    global operation2



    if entries == 0:
        if type == 1:
            operation = "add"

        elif type == 2:
            operation = "multiply"

        elif type == 3:
            operation = "subtract"

        elif type == 4:
            operation = "divide"

        entries = entries + 1
        num_1 = float(e.get())
        e.delete(0, END)

    else:
        print("Going to equal")
        if type == 1:
            operation2 = "add"

        elif type == 2:
            operation2 = "multiply"

        elif type == 3:
            operation2 = "subtract"

        elif type == 4:
            operation2 = "divide"
        equal("indirect")




def equal(source):
    global num_1
    global num_2
    global resultado
    global result
    global entries
    global operation

    print("Equal Function")

    if source == "direct":
        entries = 0
    
    resultado = 1
    num_2 = float(e.get())
    e.delete(0, END)
    
    if operation == "add":
        result = num_1 + num_2
        print("successfully read add, result is")
        print(result)

    elif operation == "multiply":
        result = num_1 * num_2

    elif operation == "subtract":
        result = num_1 - num_2

    elif operation == "divide":
        result = num_1 / num_2

    if round(result) == result:
        result = int(result)
    
    print("Entering result")
    print(result)
    e.insert(0, result)
    if source == "indirect":
        num_1 = result
        operation = operation2

#---Define Buttons!---#

w_num = 10

button_1 = Button(root, text="1", font=15, width=w_num, pady=25,command=lambda: button_click(1))
button_2 = Button(root, text="2", font=15, width=w_num, pady=25,command=lambda: button_click(2))
button_3 = Button(root, text="3", font=15, width=w_num, pady=25,command=lambda: button_click(3))
button_4 = Button(root, text="4", font=15, width=w_num, pady=25,command=lambda: button_click(4))
button_5 = Button(root, text="5", font=15, width=w_num, pady=25,command=lambda: button_click(5))
button_6 = Button(root, text="6", font=15, width=w_num, pady=25,command=lambda: button_click(6))
button_7 = Button(root, text="7", font=15, width=w_num, pady=25,command=lambda: button_click(7))
button_8 = Button(root, text="8", font=15, width=w_num, pady=25,command=lambda: button_click(8))
button_9 = Button(root, text="9", font=15, width=w_num, pady=25,command=lambda: button_click(9))
button_0 = Button(root, text="0", font=15, width=w_num, pady=25,command=lambda: button_click(0))
button_clear = Button(root, text="Clear", font=15, width=21,pady=25,command=clear)
button_equal = Button(root, text="=", font=15, width=21,pady=25,command=lambda: equal("direct"))
button_add = Button(root, text="+", font=15, width=w_num,pady=25,command=lambda: pemdas(1))
button_multiply = Button(root, text="x", font=15, width=w_num,pady=25,command=lambda: pemdas(2))
button_subtract = Button(root, text="-", font=15, width=w_num,pady=25,command=lambda: pemdas(3))
button_divide = Button(root, text="÷", font=15, width=w_num,pady=25,command=lambda: pemdas(4))

#---Putting buttons on the screen---#

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)

button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

root.mainloop()
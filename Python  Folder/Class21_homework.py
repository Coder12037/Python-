from tkinter import *

screen=Tk()
screen.geometry("1000x1000")
screen.title("Class 21 Homework")
screen.configure(bg="grey")

var=IntVar() 
c1=Checkbutton(screen, text="Pepperoni", onvalue=1, offvalue=0, variable=var)
c1.grid(row=1, column=1)
#When you have one value from only one check box do what you did(as seen below). If tehre are multiple checkboxes, add an "and" function as well ot make sure to make both parties are happy. 
def gee():
    if var.get()==1:
        l1=Label(screen, text="You don't want pepperoni")
        l1.grid(row=1, column=2)
    elif var.get()==0:
        l1=Label(screen, text="You ordered pepperoni")
        l1.grid(row=1, column=3)

b=Button(screen, text="Select toppings", command=gee)
b.grid(row=1, column=4)

screen.mainloop()
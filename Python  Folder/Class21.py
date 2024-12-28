#-------------------Chcekbutton and dropdown-----------------------------------
#Checkbox menas when we select multiple option out of all given options.
#dropdown means when we click a list opens out of which w ecan select one option.

from tkinter import *

screen=Tk()
screen.geometry("1000x1000")
screen.title("Checkbutton Dropdown")
screen.configure(bg="lightgreen")
#checkbutton
#we will create tkinter variable for all checbutton because every checkbutton will give value to it. as we know tkinter variable stores value which we type or select on screen of tkinter. 
# onvalue =1 menas if heckbox is selected then 1 will come , offvalue =0 means if ehchbox is not selected then  0 wil come in tkinter
#variable.

var=IntVar() # IntVar func because interger value iether 1 or 0 will come in variable. also connect variable with chechbox
c1=Checkbutton(screen, text="C++", onvalue=1, offvalue=0, variable=var)
var2=IntVar()
c2=Checkbutton(screen, text="Python", onvalue=1, offvalue=0, variable=var2)
c1.grid(row=0, column=0)
c2.grid(row=1, column=1)

#now wee get value from variable var and var2 and ehck if it has 1 or 0 inside that. get() function on variable
def gee():
    if var.get()==1 and var2.get()==0:
        l1=Label(screen, text="C++ is selected")
        l1.grid(row=3, column=1)
    elif var.get()==0 and var2.get()==1:
        l1=Label(screen, text="Python is selected")
        l1.grid(row=3, column=1)
    elif var.get()==1 and var2.get()==1:
        l1=Label(screen, text="C++ and Python is selected")
        l1.grid(row=3, column=1)
    else:
        l1=Label(screen, text="C++ and Python is not selected")
        l1.grid(row=3, column=1)

#Goal : We will create a button and when we click on the button then whatevery is selected in checkbutton should come as label on screen
b=Button(screen, text="Click here to get answer which will be selected", command=gee)
b.grid(row=2, column=2)

#-------------------------------------Dropdown---------------------------------------
#DropDown we use OptionMenu. In this we create one variable always
option=["Burger", "Chinese", "Indian","cake"]

var3=StringVar() #Here we use StringVar() becauyse the answer which person will select is string thye food item selected will come here in var3/ use * to give option name in d
var3.set("Fries") # this will set the start staring in optionmenu
d=OptionMenu(screen, var3, *option)
d.grid(row=4, column=0)

screen.mainloop()
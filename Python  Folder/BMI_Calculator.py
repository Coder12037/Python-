from tkinter import *
from tkinter import filedialog

screen=Tk()
screen.geometry("1000x1000")
screen.title("BMI Calculator")

l1=Label(screen, text="Height(cm)")
l1.grid(row=1,column=1)

e1=Entry(screen)
e1.grid(row=3,column=1)

l2=Label(screen, text="Weight(kg)")
l2.grid(row=1,column=3)

e2=Entry(screen)
e2.grid(row=3,column=3)

#REmember : whenver we we want to put some text inside textbox fro our side or answere we use set. but along wit that we have to create tkinter variable as well
#so firts we create tkintervariable and we connect it to entrybox e3. then we set answer in tkinter variable and from there it automatically goes to entrybox e3

#tkinter variable
s=StringVar()
e3=Entry(screen, textvariable=s) # connect s with e3 using textvariable
e3.grid(row=3,column=5)


def total():
    #Remember always putint() before entrybox or anything in tkinter if you are doing a mathematical thing.always use get() function to get value from textbox.
    r=int(e1.get())
    s1=int(e2.get())
    result=r/s1
    result1=str(result)#convert int to str as we can only give string answer to s variable
    #Remember to use set() function when we have to set text in any component
    s.set(result1)
    

l3=Label(screen, text="BMI")
l3.grid(row=1,column=5)


def clear():
    e1.delete(0, END)  # Delete text in height entry
    e2.delete(0, END)  # Delete text in weight entry
    s.set("")  # Clear the BMI result
    
b1=Button(screen, text="Clear", command=clear)
b1.grid(row=2, column=7)

b2=Button(screen, text="Calculate BMI", command=total)
b2.grid(row=4, column=7)

screen.mainloop()

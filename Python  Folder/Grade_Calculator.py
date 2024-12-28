from tkinter import *
from tkinter import filedialog

screen=Tk()
screen.geometry("500x500")
screen.title("Grade calculator")

l1=Label(screen, text="English:")
l1.grid(row=1, column=1)

e1=Entry(screen)
e1.grid(row=1, column=3)

l2=Label(screen, text="Analytical Skills:")
l2.grid(row=3, column=1)

e2=Entry(screen)
e2.grid(row=3, column=3)

l3=Label(screen, text="General Knowledge:")
l3.grid(row=5, column=1)

l4=Label(screen, text="Total:")
l4.grid(row=7, column=1)

l5=Label(screen, text="Average:")
l5.grid(row=9, column=1)

l6=Label(screen, text="Grade:")
l6.grid(row=11, column=1)

e3=Entry(screen)
e3.grid(row=5, column=3)

def calculate():
    r=int(e1.get())
    s=int(e2.get())
    t=int(e3.get())
    result=r+s+t
    #give text to l7 using config total
    l7.config(text=result)
    
    #give text to l8 using config average
    result1=(r+s+t)/3
    l8.config(text=result1)
    
    #give grade to l9 using config() we can use if then for grade.
    #First calculate percentage  then give grade
    total=(result*100)/300
    if total>90 and total <100:
        l9.config(text="Grade A")
    elif grade>=70 and grade<=90:
        l9.config(text="Grade B")
    else:
        l9.config(text="Grade C")

#config() is used to chnage property later eg : we have created a label and we want to change the label later then we can usethe config. 
#so at time when widget is created we give either no property or we give some. later if we wnat to chnage w ecan use this.
#text, color, backgrounhd-color, size, etc..
l7=Label(screen)
l7.grid(row=7, column=3)

l8=Label(screen)
l8.grid(row=9, column=3)

l9=Label(screen)
l9.grid(row=11, column=3)

b1=Button(screen, text="Calculate",command=calculate)
b1.grid(row=13, column=1)

b2=Button(screen, text="Exit", command=screen.destroy)

#To close the window: use screen.destroy()
b2.grid(row=13, column=4)

screen.mainloop()
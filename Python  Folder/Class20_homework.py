from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

screen=Tk()
screen.geometry("1000x1000")
screen.title("SLider Project")
screen.configure(bg="white") 

s=Scale

s=Scale(screen, from_=1, to=100,orient=VERTICAL ) #DO NOT ADD INSIDE BRACKET: Put it before the function because the function(def) should only have the label and nothing else inside it.  
s.grid(row=3, column=1) 

def slider():
 l1=Label(screen, text= "Vertical Scale value="+str(s.get()))
 l1.grid(row=3, column=4)#This is called after the button. Function always has the action of the item inside it. For example, the action for the click of a button would be indside the function. 

b1=Button(screen, text="Display vertical", command=slider)
b1.grid(row=3, column=2) 

screen.mainloop()

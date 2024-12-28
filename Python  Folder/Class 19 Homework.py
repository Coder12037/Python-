from tkinter import * 
from tkinter import messagebox

screen=Tk()
screen.geometry("1000x1000")
screen.title("Root window")



messagebox.showinfo("This is not","Root window")
messagebox.showwarning("Warning", "Open top level 2")
messagebox.showerror("Exit")


def call():
    messagebox.showinfo("Information", "This is nice")

b1=Button(screen, text='Click me', command=call)
b1.pack()


def screen3():
    screen3=Tk()
    l2=Label(screen3, text="")
    global screen2
    screen2.destroy()

def newscreen():
    screen.destroy()
    screen2=Tk()
    screen2.geometry("1000x1000")
    screen2.title("New srreen")
    l1=Label(screen2, text="New screen")
    l1.pack()
    b3=Button(screen2, text="Go to third screen", command=screen3)
    b3.pack()

b2=Button(screen, text="New screen", command=newscreen)
b2.pack()

mainloop()
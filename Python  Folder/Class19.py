from tkinter import * 
from tkinter import messagebox

screen=Tk()
#screen size and screeen title
screen.geometry("1000x1000")
screen.title("Messagebox and New screen")


#Messagebox means pop up message that comes on screen. For messagebox we have to import seperately.

#1. showinfo() : to show information. Any title and message can be given.
messagebox.showinfo("Information","This is good")
#2. showwarning() : to show warning
messagebox.showwarning("Wraning", "Downloaded file has some issue")
#3. showerror() : to show error
messagebox.showerror("Error", "Downloaded file is currupted")
#4. okcancel : this has ok and cancel button. ask question
messagebox.askokcancel("Info", "Do you want to to download?")
#5. yesno : this for ask question button name is change
messagebox.askyesno("Info", "Do yo want to download?")
#6. yesnocancel : this is used for ask question button name is different
messagebox.askyesnocancel("Info", "Do you want to download?")
#7. retrycancel : this is used for ask question button name is different
messagebox.askretrycancel("Info", "Do you want to download?")
#8. question : this is used for ask question button name is different
messagebox.askquestion("Info", "Do you want to donwload?")

def call():
    messagebox.showinfo("Information", "This is nice")

#remember always call using command keyword. function always creared before button as we need to call so on click of button whatever is written inside function will happen.
b1=Button(screen, text='Click me', command=call)
b1.pack()

#---------------------------------------------how to open new screen--------------------------------------
#we will create multiple screen using Tk() so that we have many pages in software.
def screen3():
    screen3=Tk()
    global screen2
    screen2.destroy()

def newscreen():
    #to craete new screen use Tk(). just change variable name. use geometry and title do everything in way screen 1 has been done
    #how to destroy on close previous screen
    screen.destroy()
    screen2=Tk()
    screen2.geometry("1000x1000")
    screen2.title("New srreen")
    #we willl creatre one label and button on second page
    l1=Label(screen2, text="New screen")
    l1.pack()
    b3=Button(screen2, text="Go to third screen", command=screen3) # now let say if you want to create third screen the create another function above this and create scree3 in that and call that function on this button
    b3.pack()

#do coding to open new screen in function abd tnen call it on button 2
b2=Button(screen, text="New screen", command=newscreen)
b2.pack()

mainloop()

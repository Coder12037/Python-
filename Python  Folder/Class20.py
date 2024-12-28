#---------------------------------file Handling-----------------------------------------
#means learning about different functions like downloading and uploading file. We will learn how to add download and upload option in a software

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

#Steps to download and upload file : 
#Defintion of Class: It is a set of fucntions, or it is is somethign where we store all our functions.

#1. first import tkinter abd import filedialog(class) as filedialog is a class which has two functions called askopenfilename, asksaveasfile
#2. then we create one function where we do coding of downloading file : For downloading file we use inbuilt function called as 
#asksaveasfile() it saves files(img, txt, python, html, css)
#3. we create second function where we do coding to upload file : we use inbuilt function asopenfilename() to open the file we upload.
#4. then we can create two buttons download and upload where we can call these functions.

screen=Tk()
screen.geometry("1000x1000")
screen.title("File Handling")
screen.configure(bg="green")

def download(): #write different filenames (.png,.jpg, etc.) which wecan download
    files=[("All files", "*.txt"), ("PNG File", "*.png"), ("Python Files", "*.py"), ("HTML File", "*.html"), ("CSS File", "*.css")]
    file=filedialog.asksaveasfile(filetypes=[("All files", "*.txt"), ("PNG File", "*.png"), ("Python Files", "*.py"), ("HTML File", "*.html"), ("CSS File", "*.css")], defaultextension=files)


b1=Button(screen, text="Download the file", command=download)
b1.grid(row=0, column=0)

def upload(): # here too we mention filetypes we will be able to upload
    filee=filedialog.askopenfilename(filetypes=[("All files", "*.txt"), ("PNG File", "*.png"), ("Python Files", "*.py"), ("HTML File", "*.html"), ("CSS File", "*.css")], mode="r")
    #If we are uploading normal text file tehnw  ecan stop here. now because we will upload img tehnw e have to do further coding  of using functions taht will  display image on screen. 
    #3 steps to display image on screen :
    #1. use Image.open(0 to give image name ).
    #2. use ImageTk.PhotoImage() to get file 
    #3. use label to display on screen
    img=ImageTk.PhotoImage(Image.open(file=filee))
    l1=Label(screen, image=img)
    l1.grid(row=1, column=1)

b2=Button(screen, text="upload the file", command=upload)
b2.grid(row=2, column=1)

#------------------------------------------------------Scale---------------------------------------------------------------
#scale means a slider where we can select numbers from any range it can be 1 to 10, 1 to 100, 20 to 40. it can be anything start and end.
#So here what will do is we will create a button  and craete a slider and select one number on slider and then when we click on button whatever number isse elcted will come as label on screen. 

def slider() :
    #herewe will create slider then we will do coding that whatever a number person selects on slider we will get that number using get function and then give it to label to dispaly on screen
    s=Scale(screen, from_=1, to=100,orient=HORIZONTAL ) #caps lock (same for vertical)
    s.grid(row=3, column=2) 
    #now get value from slier using get function
    l2=Label*(screen, text= "the value we get from scale is "+str(s.get()))
    l2.grid(row=4, column=3)


b3=Button(screen, text="Get detail value", command=slider)
b3.grid(row=5, column=3)


screen.mainloop()
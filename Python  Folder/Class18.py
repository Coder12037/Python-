#--------------------------------------Icons, Images, Frames--------------------------------------------------
#icons is used to icon on screen at the top
from tkinter import*
from PIL import ImageTk, Image

screen=Tk()
screen.geometry("1000x1000")
screen.title("Icons,Images,Frames")

#Steps to put/give icon on screen
#1. load image in variable.
#2. use iconbitmap or iconphoto to put image on screen

a=PhotoImage(file="Cristiano_PNG.png")
screen.iconphoto(False, a)

#----------------------------------Image--------------------------------------------------
#Steps to give image on screen
#1. First import imageTk, Image using PIL(pillow). ist a library which we need to install using pip command. pip install pillow
#2. Use Image.open() to open the image
#3. use resize() to adjust the size of teh image
#4. Use ImageTk.PhotoImage to give image on screen
#5. use label to display image on screen

img=Image.open("Cristiano_PNG.png")
img1=img.resize((100, 100))
img2=ImageTk.PhotoImage(img1)
l=Label(screen, image=img2)
l.pack()

#-----------------------------------------------Frame-------------------------------------------------------
#Frame means to create a box ons screen where we can put all components and widgets. liek we create one box and inside taht we place label aor button

f=Frame(screen, bg="green", borderwidth=9)
f.pack()

#when we create label, buttion inside frame make sure we give f name inside it not screen name

l1=Label(f, text="Hi This is good")
l1.pack()
b1=Button(f, text="Click here")
b1.pack()

screen.mainloop()

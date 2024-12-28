#-------------------------Bill Generator or invoice generator App----------------------------
#Here we will create one where all the customer details, product details will be entered total will calculayted and a bill in pdf will be downloaded.


#---------------------------------Assignment------------------------
#craete an interface 

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from reportlab.pdfgen import canvas

screen=Tk()
screen.geometry("1000x1000")
screen.title("Bill Generator project")
screen.configure(bg="white") 

l4=Label(screen, text="paint", font=("arial", 20))

l1=Label(screen, text="Enter your name")
l1.grid(row=1,column=1)

e1=Entry(screen)
e1.grid(row=2,column=1)

l2=Label(screen, text="Enter your email")
l2.grid(row=3,column=1)

e2=Entry(screen)
e2.grid(row=5,column=1)

l3=Label(screen,text="Enter your phone number")
l3.grid(row=6,column=1)

e3=Entry(screen)
e3.grid(row=7, column=1)

l5=Label(screen, text="Types of Paint", font=("arial", 20))
l5.grid(row=8, column=1)

var=IntVar() 
g1=Checkbutton(screen, text="Acrylic Paint", onvalue=1, offvalue=0, variable=var)
g1.grid(row=10, column=1)

var=IntVar() 
g2=Checkbutton(screen, text="Oil Paint", onvalue=1, offvalue=0, variable=var)
g2.grid(row=12, column=1)

var=IntVar() 
g3=Checkbutton(screen, text="Water Color", onvalue=1, offvalue=0, variable=var)
g3.grid(row=14, column=1)

var=IntVar() 
g4=Checkbutton(screen, text="Wall Paint", onvalue=1, offvalue=0, variable=var)
g4.grid(row=16, column=1)

def invoice():
    #we are importing the canvas, here we will put the text and then generate that as a pdf.
    if e1.get()=="" or e2.get()=="" or e3.get()=="":
        Message.showerror("error", "please enter the details")
    else:#canvas is used to draw but we will use it to put text on screen  and then convert onto pdf form and download it.
        pdffile=e1.get()+".pdf"
        c=canvas.Canvas()
        #use drawString() to put text on screen, x, y, text which we get from Entrybopx using get()
        c.drawString(50, 20, "Customer name", " ", e1.get())
        c.drawString(50, 50, "Customer Email", " ",e2.get())
        c.drawString(50,80, "Customer Email", "", e3.get())
        c.drawString(50, 110, "Paints choosen", " : ")
        c.drawString(50, 140, "Arcylic Paint : ",e4.get())
        c.drawString(50, 170, "Oil Paint : ", e5.get())
        c.drawString(50, 200, "Water Paint : ", e6.get())
        c.drawString(50, 230, "Wall Paint : ", e7.get())
        a=(int(e4.get()))*5
        b=(int(e5.get()))*7
        c=(int(e6.get()))*10
        d=(int(e7.get()))*12
        r=a+b+c+d
        c.drawString(50, 260, "Total : ", r )
        c.save()

def total():
    #here multiple each queantity with actual price and tehn add up and later use label to show on screen
        a=(int(e4.get()))*5
        b=(int(e5.get()))*7
        c=(int(e6.get()))*10
        d=(int(e7.get()))*12
        r=a+b+c+d
        l8=Label(screen, text=r)
        l8.grid(row=20, column=20)


b1=Button(screen, text="Calculate Total", command=total)
b1.grid(row=18, column=1)
#
b2= Button(screen, text="Invoice Bill", command=invoice)
b2.grid(row=18, column=3)

l6=Label(screen, text="Quantity", font=("arial", 20))
l6.grid(row=8, column=5)

e4=Entry(screen)
e4.grid(row=10, column=5)

e5=Entry(screen)
e5.grid(row=12, column=5)

e6=Entry(screen)
e6.grid(row=14, column=5)

e7=Entry(screen)
e7.grid(row=16, column=5)

l7=Label(screen, text="Price", font=("arial", 20))
l7.grid(row=8, column=10)

l8=Label(screen, text="$5")
l8.grid(row=10, column=10)

l9=Label(screen, text="$7")
l9.grid(row=12, column=10)

l10=Label(screen, text="$10")
l10.grid(row=14, column=10)

l11=Label(screen, text="$12")
l11.grid(row=16, column=10)

screen.mainloop()


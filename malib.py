from tkinter import *
from tkinter import messagebox

from quad import *
from trig import *

#functions for checking if user input is actually a number
def isnum(num):
    try:
        float(num)
        return True
    except ValueError:
        print("error")
        return False

def iseval(num):
    try:
        eval(num)
        return True
    except (ValueError, SyntaxError):
        print("error")
        return False



#while each "function" will do when selected by the listbox

def funcfunc(*args):
    func = lb.get(ACTIVE)
    for widget in FuncUI.winfo_children():
        widget.destroy()
    if func == "Quadratic Formula":

       def calcxi():
           if iseval(a.get()) and iseval(b.get()) and iseval(c.get()):
               bnum = eval(b.get().replace('^','**'))
               anum = eval(a.get().replace('^','**'))
               cnum = eval(c.get().replace('^','**'))

               if ((bnum**(2)) - 4*(anum*cnum)) < 0:
                   xtext['text'] = "There are no x-intercepts"
               elif ((bnum**(2)) - 4*(anum*cnum)) == 0:
                   xi = (-bnum)/(2*anum)
                   xtext['text'] = "The only x-intercept is (" + str(xi) + ",0)"
               else:
                   xi1 = (-bnum + (((bnum**(2)) - 4*(anum*cnum)) ** (0.5)))/(2*anum)
                   xi2 = (-bnum - (((bnum**(2)) - 4*(anum*cnum)) ** (0.5)))/(2*anum)

                   xtext['text'] = "X intercepts are (" + str(xi1) + ",0) and (" + str(xi2) + ",0)"
       
       Label(FuncUI, text="Quadratic Formula", font="Arial 16").grid(row=0, column=0)
       Label(FuncUI, text="plug in a,b, and c in ax^2 + bx + c to get the x-intercepts").grid(row=1,column=0)
       EntryFrame = Frame(FuncUI)
       EntryFrame.grid(row=2, column=0)

       Label(EntryFrame, text="a=").grid(row=0,column=0)
       a = Entry(EntryFrame, width = 4)
       a.grid(row=0,column=1)

       Label(EntryFrame, text=" b=").grid(row=0,column=2)
       b = Entry(EntryFrame, width = 4)
       b.grid(row=0,column=3)

       Label(EntryFrame, text=" c=").grid(row=0,column=4)
       c = Entry(EntryFrame, width = 4)
       c.grid(row=0,column=5)

       but = Button(EntryFrame, text="Enter", command=calcxi)
       but.grid(row=0, column=6)

       xtext = Label(FuncUI, text="")
       xtext.grid(row=3,column=0)
       
    elif func == "Quad Stand Conv":

       def getConversion():
           conv = QuadStandConv(a.get(),b.get(),c.get())
           if conv == "error":
               messagebox.showerror("Error", "Please type in real numbers")
           else:
               if conv["factor_form"]["r1"] == "na":
                   ftext['text'] = "There is no factored form of this equation"
               else:
                   ftext['text'] = "Factored Form: " + str(conv["factor_form"]["a"]) + "(x-(" + str(conv["factor_form"]["r1"]) + "))(x-("+str(conv["factor_form"]["r2"])+"))"
               vtext['text'] = "Vertex Form: " + str(conv["vertex_form"]["a"]) + "(x-(" + str(conv["vertex_form"]["h"]) + "))^2 + " + str(conv["vertex_form"]["k"])
        
       Label(FuncUI, text="Standard Form Converter", font="Arial 16").grid(row=0, column=0)
       Label(FuncUI, text="Plug in a,b, and c to get converted equation.").grid(row=1,column=0)
       EntryFrame = Frame(FuncUI)
       EntryFrame.grid(row=2, column=0)

       Label(EntryFrame, text="a=").grid(row=0,column=0)
       a = Entry(EntryFrame, width = 4)
       a.grid(row=0,column=1)

       Label(EntryFrame, text=" b=").grid(row=0,column=2)
       b = Entry(EntryFrame, width = 4)
       b.grid(row=0,column=3)

       Label(EntryFrame, text=" c=").grid(row=0,column=4)
       c = Entry(EntryFrame, width = 4)
       c.grid(row=0,column=5)

       but = Button(EntryFrame, text="Enter", command=getConversion)
       but.grid(row=0, column=6)

       ftext = Label(FuncUI, text="")
       ftext.grid(row=3,column=0)

       vtext = Label(FuncUI, text="")
       vtext.grid(row=4,column=0)
    elif func == "Quad Factor Conv":
       def getConversion():
           conv = QuadFacConv(a.get(),r1.get(),r2.get())
           if conv == "error":
               messagebox.showerror("Error", "Please type in real numbers")
           else:
               stext['text'] = "Standard Form: " + str(conv["standard_form"]["a"]) + "x^2 + " + str(conv["standard_form"]["b"]) + "x + " + str(conv["standard_form"]["c"])
               vtext['text'] = "Vertex Form: " + str(conv["vertex_form"]["a"]) + "(x-(" + str(conv["vertex_form"]["h"]) + "))^2 + " + str(conv["vertex_form"]["k"])
       Label(FuncUI, text="Factored Form Converter", font="Arial 16").grid(row=0, column=0)
       Label(FuncUI, text="Convert a(x-r1)(x-r2) to other forms.").grid(row=1,column=0)
       EntryFrame = Frame(FuncUI)
       EntryFrame.grid(row=2, column=0)

       Label(EntryFrame, text="a=").grid(row=0,column=0)
       a = Entry(EntryFrame, width = 4)
       a.grid(row=0,column=1)

       Label(EntryFrame, text=" 1st root=").grid(row=0,column=2)
       r1 = Entry(EntryFrame, width = 4)
       r1.grid(row=0,column=3)

       Label(EntryFrame, text=" 2nd root=").grid(row=0,column=4)
       r2 = Entry(EntryFrame, width = 4)
       r2.grid(row=0,column=5)

       but = Button(EntryFrame, text="Enter", command=getConversion)
       but.grid(row=0, column=6)

       vtext = Label(FuncUI, text="")
       vtext.grid(row=3,column=0)

       stext = Label(FuncUI, text="")
       stext.grid(row=4,column=0)
    elif func == "Quad Vertex Conv":
       def getConversion():
           conv = QuadVertConv(a.get(),h.get(),k.get())
           if conv == "error":
               messagebox.showerror("Error", "Please type in real numbers")
           else:
               if conv["factor_form"]["r1"] == "na":
                   ftext['text'] = "There is no factored form of this equation"
               else:
                   ftext['text'] = "Factored Form: " + str(conv["factor_form"]["a"]) + "(x-(" + str(conv["factor_form"]["r1"]) + "))(x-("+str(conv["factor_form"]["r2"])+"))"
               stext['text'] = "Standard Form: " + str(conv["standard_form"]["a"]) + "x^2 + " + str(conv["standard_form"]["b"]) + "x + " + str(conv["standard_form"]["c"])
        
       Label(FuncUI, text="Vertex Form Converter", font="Arial 16").grid(row=0, column=0)
       Label(FuncUI, text="Convert a(x-h)^2 + k to other forms.").grid(row=1,column=0)
       EntryFrame = Frame(FuncUI)
       EntryFrame.grid(row=2, column=0)

       Label(EntryFrame, text="a=").grid(row=0,column=0)
       a = Entry(EntryFrame, width = 4)
       a.grid(row=0,column=1)

       Label(EntryFrame, text=" h=").grid(row=0,column=2)
       h = Entry(EntryFrame, width = 4)
       h.grid(row=0,column=3)

       Label(EntryFrame, text=" k=").grid(row=0,column=4)
       k = Entry(EntryFrame, width = 4)
       k.grid(row=0,column=5)

       but = Button(EntryFrame, text="Enter", command=getConversion)
       but.grid(row=0, column=6)

       ftext = Label(FuncUI, text="")
       ftext.grid(row=3,column=0)

       stext = Label(FuncUI, text="")
       stext.grid(row=4,column=0)
    elif func == 'Right Triangle Trig':

        def getUnknown():
            tvars = getTrigs(angle.get(),op.get(),hy.get(),ad.get())
            if tvars == "not-enough-info":
                messagebox.showerror("Error", "Not enough information to calculate")
            else:
                #anstr.set(str(tvars['angle']))
                angle.delete(0,END)
                angle.insert(END,str(tvars['angle']))

                #hystr.set(str(tvars['hy']))
                hy.delete(0,END)
                hy.insert(END,str(tvars['hy']))

                #opstr.set(str(tvars['op']))
                op.delete(0,END)
                op.insert(END,str(tvars['op']))

                #adstr.set(str(tvars['ad']))
                ad.delete(0,END)
                ad.insert(END,str(tvars['ad']))
        
        Label(FuncUI,text="Right Triangle Solver", font = "Arial 16").grid(row=0,column=0)
        Label(FuncUI,text="Get all sides and Theta by plugging in two.").grid(row=1,column=0)

        EntryFrame = Frame(FuncUI)
        EntryFrame.grid(row=2,column=0)

        InputFrame = Frame(EntryFrame)
        InputFrame.grid(row=0,column=0)

        canvas = Canvas(EntryFrame, width=190, height=178)
        canvas.grid(row=0,column=1)

        global rightTriImg
        rightTriImg = PhotoImage(file="trianglepic.gif")
        canvas.create_image(95,89,image=rightTriImg)

        Label(InputFrame, text="Theta (degrees only)=").grid(row=0,column=0)
        #anstr = StringVar()
        angle = Entry(InputFrame)
        angle.grid(row=0,column=1)

        Label(InputFrame, text="Opposite=").grid(row=1,column=0)
        #opstr = StringVar()
        op = Entry(InputFrame)
        op.grid(row=1,column=1)

        Label(InputFrame, text="Adjacent=").grid(row=2,column=0)
        #adstr = StringVar()
        ad = Entry(InputFrame)
        ad.grid(row=2,column=1)

        Label(InputFrame, text="Hypotenuse=").grid(row=3,column=0)
        #hystr = StringVar()
        hy = Entry(InputFrame)
        hy.grid(row=3,column=1)

        goButton = Button(InputFrame, text='Get unknown', command=getUnknown)
        goButton.grid(row=4,column=0)
       
#List of all functions
funclist = [
    "Quadratic Formula",
    "Quad Stand Conv",
    "Quad Vertex Conv",
    "Quad Factor Conv",
    'Right Triangle Trig'
]

#Dictionary with key words and functions applying to them
funcdic = {
    "geometry":["Quadratic Formula","Quad Stand Conv","Quad Vertex Conv","Quad Factor Conv",'Right Triangle Trig'],
    "functions":["Quadratic Formula","Quad Stand Conv","Quad Vertex Conv","Quad Factor Conv"],
    "quadratic":["Quadratic Formula","Quad Stand Conv","Quad Vertex Conv","Quad Factor Conv"],
    "algebra":["Quadratic Formula","Quad Stand Conv","Quad Vertex Conv","Quad Factor Conv"],
    "convert":["Quad Stand Conv","Quad Vertex Conv","Quad Factor Conv"],
    "trigonometry":['Right Triangle Trig']
}


actscreen = Tk()
actscreen.title("MaLib")

screen = Frame(actscreen, bg="black")
screen.grid(row=0,column=0)

title = Label(screen, text="MaLib", font="Arial 24", bg="red", fg="white")
title.grid(row=0,column=0,pady=5)

Label(screen, text="Search for a function using a key term and get an easy tool!",bg="red",fg="white",bd=5,relief=RIDGE).grid(row=1,column=0)

#Search UI
searchframe = Frame(screen, bd=5, relief="groove",bg="red")
searchframe.grid(row=2, column=0,pady=5)

Label(searchframe,text="Search with a catagory: ",bg="red",fg="white").grid(row=0,column=0)

def ResetLb(*args):
    lb.delete(0,END)
    if cursearch.get() == 'all':
        for func in funclist:
            lb.insert(END, func)
    else:
        for func in funcdic[cursearch.get()]:
            lb.insert(END, func)

cursearch = StringVar()
searchterms = list(funcdic.keys())
searchterms = ['all'] + searchterms
cursearch.set('all')

options = OptionMenu(searchframe, cursearch, *searchterms)
options.grid(row=0,column=1)

#assign a function to when dropdown is cahnged
cursearch.trace('w', ResetLb)


#Function List and Function UI Frames

Bottom = Frame(screen, bg="black")
Bottom.grid(row=3,column=0, sticky=W)

lb = Listbox(Bottom, borderwidth=2, relief="groove",bg="blue", fg="white")
for func in funclist:
    lb.insert(END, func)
lb.bind('<Double-Button-1>', funcfunc)

lb.grid(row=0,column=0,sticky=W)

FuncUI = Frame(Bottom, bd=5, relief=RAISED)
FuncUI.grid(row=0,column=1,sticky=W,padx=5)


actscreen.resizable(False,False)

actscreen.mainloop()

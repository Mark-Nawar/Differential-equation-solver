import math
from tkinter import *
root = Tk()
#title and size
root.title("RUNGE KUTTAH")
root.geometry("1050x302")

#label of the title
title =Label(root,text="Runge Kuttah calculator",fg="blue",font=("Times New Roman",20))
title.grid(column=1,columnspan=6,row =0)
###############################CASE1 first derv.#####################################################
def dydx(x, y):
    return (eval(entry1.get()))

def rungeKutta():
    # Count number of iterations using step size
    # step height h
    x0 = float(entry2.get())
    y0 = float(entry3.get())
    x = float(entry5.get())
    h=x-x0
    if(x0==0 and y0==0 and h==0 and x==0):
        return
    text_field.delete(0.0,'end')
    n = (int)((x - x0) / h)
    # Iterate for number of iterations
    y = y0
    for i in range(1, n + 1):
        #"Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * dydx(x0 + h, y + k3)

        # Update next value of y
        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

        # Update next value of x
        x0 = x0 + h
    text_field.insert(0.0,y)

####GUI for case 1---------->
title1 =Label(root,text="Case 1 First der.",font=("Times New Roman",10))
title1.grid(columnspan=2,row=1)
#label of the case one condition f(x,y) y' and x0 y0 h and x needed  5 labels
title1 =Label(root,text="F(x,y)",font=("Times New Roman",10))
title1.grid(column=0,row=2)
entry1= Entry(root)
entry1.grid(column=1,row=2)

title2 =Label(root,text="x0",font=("Times New Roman",10))
title2.grid(column=0,row=3)
entry2= Entry(root)
entry2.grid(column=1,row=3)

title3 =Label(root,text="y0",font=("Times New Roman",10))
title3.grid(column=0,row=4)
entry3= Entry(root)
entry3.grid(column=1,row=4)

title5 =Label(root,text="x",font=("Times New Roman",10))
title5.grid(column=0,row=5)
entry5= Entry(root)
entry5.grid(column=1,row=5)

title6 =Label(root,text="Y=",font=("Times New Roman",10))
title6.grid(column=0,row=6)
text_field = Text(root,height=1,width=10)
text_field.grid(column=1,row=6)

button1=Button(root,text="Execute",bg="purple",fg="white",font=("Times New Roman",15),command=rungeKutta)
button1.grid(columnspan=2,row=7)
#########################################################CASE1 DONE####################################################
##################################################CASE 2 Second Derv.############################################

def f2(x, y,z):
    return (eval(entry12.get()))

def rungeKutta2():
    # Count number of iterations using step size
    # step height h
    x0=float(entry22.get())
    y0=float(entry32.get())
    x=float(entry52.get())
    z0=float(entry522.get())
    h=x-x0
    if(x0==0 and y0==0 and h==0 and x==0):
        return
    text_field.delete(0.0,'end')
    y = y0
    z=z0

    m1 = f2(x0, y0, z0)
    k1 = z
    k2 = z + (m1 * h) / 2.0
    m2 = f2((x0 + h / 2.0), (y0 + (k1 * h) / 2.0), k2)
    k3 = z + m2 * h / 2.0
    m3 = f2((x0 + h / 2.0), (y0 + k2 * h / 2.0), k3)
    k4 = z + m3 * h
    m4 = f2((x0 + h), (y0 + k3 * h), k4)
    m = ((m1 + 2 * m2 + 2 * m3 + m4) / 6)
    k = ((k1 + 2 * k2 + 2 * k3 + k4) / 6)
    z = z + m * h
    y = y + k * h
    x = x + h
    text_field2.insert(0.0,y)
    text_field22.insert(0.0,z)


####GUI for case 2---------->
title12 =Label(root,text="Case 2 Second der.",font=("Times New Roman",10))
title12.grid(column=3,columnspan=2,row=1)
#label of the case one condition f(x,y) y' and x0 y0 h and x needed  5 labels
title112 =Label(root,text="F(x,y,z(y'))",font=("Times New Roman",10))
title112.grid(column=3,row=2)
entry12= Entry(root)
entry12.grid(column=4,row=2)

title22 =Label(root,text="x0",font=("Times New Roman",10))
title22.grid(column=3,row=3)
entry22= Entry(root)
entry22.grid(column=4,row=3)

title32 =Label(root,text="y0",font=("Times New Roman",10))
title32.grid(column=3,row=4)
entry32= Entry(root)
entry32.grid(column=4,row=4)

title52 =Label(root,text="x",font=("Times New Roman",10))
title52.grid(column=3,row=5)
entry52= Entry(root)
entry52.grid(column=4,row=5)

title522 =Label(root,text="z0",font=("Times New Roman",10))
title522.grid(column=3,row=6)
entry522= Entry(root)
entry522.grid(column=4,row=6)

title62 =Label(root,text="Y=",font=("Times New Roman",10))
title62.grid(column=3,row=7)
text_field2 = Text(root,height=1,width=10)
text_field2.grid(column=4,row=7)
title622 =Label(root,text="Z=",font=("Times New Roman",10))
title622.grid(column=3,row=8)
text_field22 = Text(root,height=1,width=10)
text_field22.grid(column=4,row=8)

button2=Button(root,text="Execute",bg="green",fg="white",font=("Times New Roman",15),command=rungeKutta2)
button2.grid(column=3,columnspan=3,row=9)
#########################################CASE2 DONE###################################################
#########################################CASE 3 (two equations)#######################################
######case 3 logic
def mm3(x,y,z):
    return (eval(entry1132.get()))
def f23(x, y,z):
    return (eval(entry113.get()))

def rungeKutta3():
    # Count number of iterations using step size
    # step height h
    x0=float(entry223.get())
    y0=float(entry33.get())
    x=float(entry53.get())
    z0=float(entry523.get())
    h=x-x0
    if(x0==0 and y0==0 and h==0 and x==0):
        return
    text_field.delete(0.0,'end')
    y = y0
    z=z0
    x = x0
    y = y0
    z = z0
    m1 = mm3(x0, y0, z0)
    k1 = f23(x0, y0, z0)
    k2 = f23((x0 + h / 2.0), (y0 + (k1 * h) / 2.0), (z0 + (m1 * h) / 2.0))
    m2 = mm3((x0 + h / 2.0), (y0 + (k1 * h) / 2.0), (z0 + (m1 * h) / 2.0))
    k3 = f23((x0 + h / 2.0), (y0 + k2 * h / 2.0), (z0 + (m2 * h) / 2.0))
    m3 = mm3((x0 + h / 2.0), (y0 + k2 * h / 2.0), (z0 + (m2 * h) / 2.0))
    k4 = f23((x0 + h), (y0 + k3 * h), (z0 + m3 * h))
    m4 = mm3((x0 + h), (y0 + k3 * h), (z0 + m3 * h))
    m = ((m1 + 2 * m2 + 2 * m3 + m4) / 6)
    k = ((k1 + 2 * k2 + 2 * k3 + k4) / 6)
    z = z + m * h
    y = y + k * h
    text_field23.insert(0.0,y)
    text_field232.insert(0.0,z)
####GUI for case 3---------->
title13 =Label(root,text="Case3 2 equations",font=("Times New Roman",10))
title13.grid(column=5,columnspan=2,row=1)
#label of the case one condition f(x,y) y' and x0 y0 h and x needed  5 labels
title113 =Label(root,text="Y'",font=("Times New Roman",10))
title113.grid(column=5,row=2)
entry113= Entry(root)
entry113.grid(column=6,row=2)
title1132 =Label(root,text="Z'",font=("Times New Roman",10))
title1132.grid(column=5,row=3)
entry1132= Entry(root)
entry1132.grid(column=6,row=3)

title223 =Label(root,text="x0",font=("Times New Roman",10))
title223.grid(column=5,row=4)
entry223= Entry(root)
entry223.grid(column=6,row=4)

title33 =Label(root,text="y0",font=("Times New Roman",10))
title33.grid(column=5,row=5)
entry33= Entry(root)
entry33.grid(column=6,row=5)

title53 =Label(root,text="x",font=("Times New Roman",10))
title53.grid(column=5,row=6)
entry53= Entry(root)
entry53.grid(column=6,row=6)

title523 =Label(root,text="z0",font=("Times New Roman",10))
title523.grid(column=5,row=7)
entry523= Entry(root)
entry523.grid(column=6,row=7)

title62 =Label(root,text="Y=",font=("Times New Roman",10))
title62.grid(column=5,row=8)
text_field23 = Text(root,height=1,width=10)
text_field23.grid(column=6,row=8)
title622 =Label(root,text="Z=",font=("Times New Roman",10))
title622.grid(column=5,row=9)
text_field232 = Text(root,height=1,width=10)
text_field232.grid(column=6,row=9)

button3=Button(root,text="Execute",bg="black",fg="white",font=("Times New Roman",15),command=rungeKutta3)
button3.grid(column=5,columnspan=2,row=10)
###############################case 3 done ########################
###############some important notes################################
titlel =Label(root,text="Notes:This code is written in Python:",font=("Times New Roman",10))
titlel.grid(column=9,row=3)
titlel2 =Label(root,text="1)if you want to use power (x^2)--->(x**2) or (e^y)-->(math.exp(y) ",font=("Times New Roman",10))
titlel2.grid(column=9,row=4)
titlel3 =Label(root,text="2)if you want to use trig.(sin(x)-->(math.sin(x)) or (pi)-->(math.pi) ",font=("Times New Roman",10))
titlel3.grid(column=9,row=5)
titlel4 =Label(root,text="3)this is a case-sensitive language so enter the functions in lowercase(x,y,z),where (z)replaces (y')",font=("Times New Roman",10))
titlel4.grid(column=9,row=6)
titlel5 =Label(root,text="4)multiple cases could be executed independently",font=("Times New Roman",10))
titlel5.grid(column=9,row=7)
titlel6 =Label(root,text="created by Mark-Nawar CCE 23",font=("Times New Roman",10))
titlel6.grid(column=9,row=10)
root.mainloop()


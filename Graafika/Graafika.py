from tkinter import *
from math import *
import numpy as np
import matplotlib.pyplot as plt

def lahenda_klikkid():
    if ent1.get()=="": 
        ent1.configure(bg="red")
    else:
        ent1.configure(bg="lightblue")
    if ent2.get()=="": 
        ent2.configure(bg="red")
    else:
        ent2.configure(bg="lightblue")
    if ent3.get()=="": 
        ent3.configure(bg="red")
    else:
        ent3.configure(bg="lightblue")
    if ent1.get()!="" and ent2.get()!="" and ent3.get()!="":
        a=float(ent1.get())
        b=float(ent2.get())
        c=float(ent3.get())
        D=b*b-4*a*c
        if D>0:
            x1=round((-b-sqrt(D))/(2*a),2)
            x2=round((-b+sqrt(D))/(2*a),2)
            vas=f"X1={x1} \nX2={x2}"
        elif D==0:
            x1=round((-1*b)/(2*a),2)
            vas=f"X1={x1}"
        else:
            vas="Lahendust pole"
        lbl0.configure(text=vas)
        
def graafik():
    a=float(ent1.get())
    b=float(ent2.get())
    c=float(ent3.get())
    x0=(-b)/2*a
    y0=a*x0*x0+b*x0+c
    x=np.arange(x0-15,x0+15,1)#min,max,step
    y=a*x*x+b*x+c
    fig=plt.figure()
    plt.plot(x,y,'r-d')
    plt.title("Ruutvõrrand")
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.grid(True)
    plt.show()
   
aken=Tk()
aken.geometry("800x600")
aken.title("Ruutvõrrandi lahendus")

lbl=Label(aken,text="Ruutvõrrandi lahendus",bg="gold",fg="#AA4A44",font="Arial 20",height=5,width=20)
ent1=Entry(aken,fg="blue",bg="lightblue",width=3,font="Arial 20",justify=LEFT)
lbl1=Label(aken,text="x**2+",font="Arial 20",height=5,width=10)
ent2=Entry(aken,fg="blue",bg="lightblue",width=3,font="Arial 20",justify=LEFT)
lbl2=Label(aken,text="x+",font="Arial 20",height=5,width=10)
ent3=Entry(aken,fg="blue",bg="lightblue",width=3,font="Arial 20",justify=LEFT)
lbl3=Label(aken,text="=0",font="Arial 20",height=5,width=10)
btn=Button(aken,text="Lahenda",fg="blue",bg="lightblue",width=10,font="Arial 20",justify=LEFT, command=lahenda_klikkid)
lbl0=Label(aken,text="Lahendus",bg="gold",fg="#AA4A44",font="Arial 20",height=5,width=20)
btn_g=Button(aken,text="Graafik", font="Calibri 26",bg="green",command=graafik)


lbl.pack()
ent1.pack(side=LEFT)
lbl1.pack(side=LEFT)
ent2.pack(side=LEFT)
lbl2.pack(side=LEFT)
ent3.pack(side=LEFT)
lbl3.pack(side=LEFT)
btn.pack(side=LEFT)
lbl0.place(x=235,y=450)
btn_g.place(x=650,y=425)
aken.mainloop()


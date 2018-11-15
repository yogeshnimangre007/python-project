# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:38:26 2018

@author: OptimusPrime
"""

from tkinter import *
from tkinter import messagebox
import os
def open_student():
    os.system('superwiser.py')
def open_form():
    os.system('newsup.py')
def login():
    f=open("validate.txt","r")
    for line in f:
        data=line.split()
        if(data[0]==entry_1.get() and data[1]==entry_2.get()):
           c=1
           break
        else:
           c=2
    if(c==1):
        os.system('supfinal.py')
    if(c==2):
        messagebox.showerror("ERROR","NO such USER FOUND")
    
root = Tk()

root.title("LOGIN PAGE")

label_0=Label(root,text="LOGIN PAGE",width=20,bg='black',fg='white',font=("bold",20))
label_0.place(x=300,y=53)


label_1=Label(root, text="USERNAME : ", width=20,fg='black',font=("bold",10))
label_1.place(x=350,y=130)

entry_1=Entry(root)
entry_1.place(x=600,y=130)

label_2=Label(root,text="password : ",width=20,fg='black',font=("bold",10))
label_2.place(x=350,y=180)

entry_2=Entry(root)
entry_2.place(x=600,y=180)

Button(root,text='LOGIN',width=20,bg='skyblue',fg='black',command=login).place(x=550,y=250)
Button(root,text='NEW USER',width=20,bg='skyblue',fg='black',command=open_form).place(x=750,y=250)
Button(root,text='QUIT',width=20,bg='skyblue',fg='black',command=quit).place(x=950,y=250)
Button(root,text='BACK',width=20,bg='skyblue',fg='black',command=open_student).place(x=1150,y=250)

root.mainloop()


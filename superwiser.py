# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:25:03 2018

@author: OptimusPrime
"""

from tkinter import*
import os
def open_student():
    os.system('student.py')
def open_login():
    os.system('pythonloginpagec.py')
def open_newsup():
    os.system('newsup.py')
root = Tk()
root.title("SUPERWISER")

label_0=Label(root,text="WELCOME",width=20,bg='black',fg='white',font=("bold",20))
label_0.place(x=0,y=53)




Button(root,text="LOGIN PAGE",width=20,bg='skyblue',fg='black',command=open_login).place(x=150,y=150)
Button(root,text="CREAT ACCOUNT",width=20,bg='skyblue',fg='black',command=open_newsup).place(x=350,y=150)
Button(root,text='QUIT',width=20,bg='skyblue',fg='black',command=quit).place(x=550,y=150)
Button(root,text='BACK',width=20,bg='skyblue',fg='black',command=open_student).place(x=750,y=150)

root.mainloop()

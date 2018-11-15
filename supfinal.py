# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:40:16 2018

@author: OptimusPrime
"""

from tkinter import*
from tkinter import messagebox
import os
def open_pythonloginpage():
    if(os.stat("caption.txt").st_size == 0):
        
        messagebox.showerror("ERROR","NO ALLOCATION DONE")
        
    os.system('caption.txt')
root = Tk()
root.title("CONFIRM")
label_0=Label(root,text="click for caption file",width=30,bg='black',fg='white',font=("italic",10))
label_0.place(x=500,y=53)
Button(root,text="OK",width=20,bg='skyblue',fg='black',command=open_pythonloginpage).place(x=550,y=440)
root.mainloop()
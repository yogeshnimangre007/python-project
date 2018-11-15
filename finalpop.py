# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:34:27 2018

@author: OptimusPrime
"""

from tkinter import*
import os
root = Tk()
root.title("DONE")
label_0=Label(root,text="YOU ARE SUCCESSFULLY REGISTERED",width=30,bg='black',fg='white',font=("italic",10))
label_0.place(x=500,y=53)
Button(root,text="DONE",width=20,bg='skyblue',fg='black',command=quit).place(x=550,y=440)
root.mainloop()
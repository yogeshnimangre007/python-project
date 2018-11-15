

from tkinter import*
import os
def open_pythonloginpage():
    os.system('pythonloginpagec.py')
root = Tk()
root.title("CONFIRM")
label_0=Label(root,text="YOU ARE SUCCESSFULLY REGISTERED",width=30,bg='black',fg='white',font=("italic",10))
label_0.place(x=500,y=53)
Button(root,text="OK",width=20,bg='skyblue',fg='black',command=open_pythonloginpage).place(x=550,y=440)
root.mainloop()
from tkinter import*
import os
def open_login(): 
    os.system('pythonloginpage.py')
def open_creatstudent():
    os.system('ns.py')
def open_superwiser():
    os.system('superwiser.py')
root = Tk()
#img = im.PhotoImage(C:\Users\OptimusPrime\Desktop\python project\jkl.)

root.title("STUDENT")
label_0=Label(root,text="WELCOME",width=20,bg='black',fg='white',font=("bold",20))
label_0.place(x=0,y=53)
Button(root,text="LOGIN PAGE",width=20,bg='skyblue',fg='black',command=open_login).place(x=150,y=150)
Button(root,text="CREAT STUDENT ACCOUNT",width=20,bg='skyblue',fg='black',command=open_creatstudent).place(x=350,y=150)
Button(root,text="FOR SUPERVISOR",width=20,bg='skyblue',fg='black',command=open_superwiser).place(x=550,y=150)
Button(root,text="Quit",width=20,bg='skyblue',fg='black',command=quit).place(x=750,y=150)
root.mainloop()

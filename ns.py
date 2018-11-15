from tkinter import *
from tkinter import messagebox
#import pandas as pd
import os
def open_student():
    os.system('student.py')
def write_to_file():
    name=entry_1.get()
    regno=entry_2.get()
    password=entry_6.get()
    projectname=entry_3.get()
    mobileno=entry_4.get()
    email=entry_5.get()
    k=email.count('@')
    if(k==1 and len(mobileno)==10):
        file=open("record.txt","a")
        file.write("Name :"+name+"\n"+"Reg .no :"+regno+"\n"+"Password :"+password+"\n"+"project name :"+projectname+"\n"+"Mobile no"+mobileno+"\n"+"E-mail :"+email+"\n"+"--------------------------------------------"+"\n")
        g=open("validate.txt","a")
        g.write(name+" "+password+"\n")
        os.system('pop.py')
    else:
        messagebox.showerror("ERROR","%Invalid data entered,please asuure that email and phone number entered are correct")
    
'''
    try:
        Data = pd.read_csv('Data.csv')
        s1=pd.Series([name,password],index=["username","password"])
        Data = Data.append(s1,ignore_index=True)
        Data.to_csv('Data.csv',index=False)
    except FileNotFoundError:
        
        Data = pd.DataFrame(columns=['username','password'])
        s1=pd.Series([name,password],index=["username","password"])
        Data = Data.append(s1,ignore_index=True)
        Data.to_csv('Data.csv',index=False)
'''  
         
          
    
   
root = Tk()

root.title("NEW USER STUDENT")

label_0=Label(root,text="NEW USER STUDENT:",width=20,bg='black',fg='white',font=("bold",20))
label_0.place(x=300,y=53)

label_1=Label(root,text="NAME :",width=20,font=("bold",10))
label_1.place(x=350,y=130)

entry_1 = Entry(root)
entry_1.place(x=500,y=130)

label_2=Label(root,text="Reg.No :",width=20,font=("bold",10))
label_2.place(x=350,y=180 )

entry_2 = Entry(root)
entry_2.place(x=500,y=180)

label_6=Label(root,text="password : ",width=20,fg='black',font=("bold",10))
label_6.place(x=350,y=230)

entry_6=Entry(root)
entry_6.place(x=500,y=230)


label_3=Label(root,text="project name :",width=20,font=("bold",10))
label_3.place(x=350,y=280)

entry_3 = Entry(root)
entry_3.place(x=500,y=280)

label_4= Label(root,text="Mobile.No :",width=20,font=("bold",10))
label_4.place(x=350,y=330)

entry_4 = Entry (root)
entry_4.place(x=500,y=330)

label_5=Label(root,text="Email.id :",width=20,font=("bold",10))
label_5.place(x=350,y=380)

entry_5 = Entry(root)
entry_5.place(x=500,y=380)

Button(root,text="Register",width=20,bg='skyblue',fg='black',command=write_to_file).place(x=550,y=440)
Button(root,text='QUIT',width=20,bg='skyblue',fg='black',command=quit).place(x=750,y=440)
Button(root,text='BACK',width=20,bg='skyblue',fg='black',command=open_student).place(x=950,y=440)
root.mainloop()

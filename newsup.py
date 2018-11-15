from tkinter import*
import os
def open_student():
    os.system('superwiser.py')
def write_to_file():
    name=entry_1.get()
    uid=entry_2.get()
    password=entry_6.get()
    projectname=entry_3.get()
    mobileno=entry_4.get()
    email=entry_5.get()
    file=open("record_superviser.txt","a")
    file.write("Name :"+name+"\n"+"UID .no :"+uid+"\n"+"Password :"+password+"\n"+"project name :"+projectname+"\n"+"Mobile no"+mobileno+"\n"+"E-mail :"+email+"\n"+"--------------------------------------------"+"\n")
    file.close()
    h=open("list.txt","a")
    h.write(name+"("+uid+")"+"\n")
    g=open("validate.txt","a")
    g.write(name+" "+password+"\n")
    os.system('popc.py')
root = Tk()

root.title("NEW USER SUPERVISOR")

label_0=Label(root,text="NEW USER SUPERVISOR",width=30,bg='black',fg='white',font=("italic",20))
label_0.place(x=300,y=53)

label_1=Label(root,text="NAME :",width=20,font=("bold",10))
label_1.place(x=350,y=130)

entry_1 = Entry(root)
entry_1.place(x=500,y=130)

label_2=Label(root,text="UID :",width=20,font=("bold",10))
label_2.place(x=350,y=180 )

entry_2 = Entry(root)
entry_2.place(x=500,y=180)


label_6=Label(root,text="password : ",width=20,fg='black',font=("bold",10))
label_6.place(x=350,y=230)

entry_6=Entry(root)
entry_6.place(x=500,y=230)

label_3=Label(root,text="specialization :",width=20,font=("bold",10))
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

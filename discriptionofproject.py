from tkinter import*
import os
def done():
    s=entry_1.get()
    su=entry_2.get()
    file=open("caption.txt","a")
    last=s+"------>"+su+"\n"
    file.write(last)
    os.system('finalpop.py')
def view_list():
    os.system('list.txt')
root = Tk()

root.title("Castone Project Supervisor Allocation")

label_0 =Label(root,text="Capstone Project Supervisor Allocation",width=50, bg ='skyblue',fg='black',font=("bold",20))
label_0.place(x=0,y=33)

label_1 = Label(root, text ="  > The capstone project is a two semester process in which students pursue independent research on a question or problem of their choice",width=0,font=("bold",10))
label_1.place(x=0,y=100)

label_2 =Label(root,text = "  >Engage with the scholorly debates in the relevent disciplines and with the guidenceof a faculty mentor _ produces a substutional paper that reflects a deep understanding of the topic",width=0,font=("bold",10))
label_2.place(x=0,y=150)

label_3 = Label(root, text="  >Students are strongly encouraged to choose a topic in which they have some competence based on their academic work,proffesional experience or exploration of future career options",width=0,font=("bold",10))
label_3.place(x=0 ,y=200)

label_4 = Label(root , text ="  >The Capstone Project is both a valuable intellectual experienceand also a vechile through which students can demonstrate their research , analytical, and writing skills to either prospective employors or graduate and professional schools.",width=0,font=("bold",10))
label_4.place(x=0,y=250)

label_4 = Label(root , text ="  Click the button to se list of supervisers and related info.",width=0,font=("bold",10))
label_4.place(x=0,y=300)

Button(root, text ="LIST",width=10,bg='skyblue',fg='black',font=("bold",10),command=view_list).place(x=00,y=400)

label_1=Label(root,text="STUDENT NAME(registration no in brackets) :",width=50,font=("bold",10))
label_1.place(x=100,y=500)

entry_1 = Entry(root)
entry_1.place(x=500,y=500)

label_2=Label(root,text="SUPERVISER NAME (UID no is brackets) :",width=50,font=("bold",10))
label_2.place(x=100,y=550 )

entry_2 = Entry(root)
entry_2.place(x=500,y=550)

Button(root, text ="DONE",width=20,bg='skyblue',fg='black',font=("bold",10),command=done).place(x=500,y=600)

root.mainloop()

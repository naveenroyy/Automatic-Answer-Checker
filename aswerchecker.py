from tkinter import *;
from PIL import ImageTk;
from PIL import Image;
from tkinter import messagebox;
import pandas as pd;
import sqlite3
class Answer_checker:
    def __init__(self,root):
        self.root=root
        self.root.title("Automatic Answer Checker")
        self.root.geometry("1050x650+1+1")
        self.bgl=Label(root,image=bg_icon).place(x=1,y=1)
        self.label1=Label(root,text="Automatic Answer Checker",width=30, fg='black', bg='white',font=("arial",22,"bold"))
        self.label1.place(x=300,y=100)
        
        self.button1=Button(root,text="USER",width=10,height=5, fg='black', bg='white',command=self.printa)
#button1.geometry("100x100")
        self.button2=Button(root,text="ADMIN",width=10,height=5, fg='black', bg='white',command=self.admin)
        self.button2.pack()
        self.button2.place(x=400,y=250)
#button1.grid(row=0,column=6,pady=50,padx=100)
        self.button1.pack()
        self.button1.place(x=600,y=250)
    def printa(self):
        self.root1=Toplevel(root)
        self.root1.title("User")
        self.root1.geometry("1050x650+1+1")
        bg =Label(self.root1,image=bg_icon).place(x=1,y=1)
        self.l1=Label(self.root1,text="User Domain",width=30,  fg='black', bg='white',font=("arial",22,"bold"))
        self.l1.place(x=300,y=100)
        self.b1=Button(self.root1,text="login",width=10,height=5, fg='black', bg='white',command=self.log_in)
       # b1.pack()
        self.b1.place(x=600,y=250)
        self.b2=Button(self.root1,text="Register",width=10,height=5, fg='black', bg='white',command=self.Register)
        #b2.pack()
        self.b2.place(x=400,y=250)
        
        
    def printb(self):

            exit()
    def admin(self):
            root2=Toplevel(root)
            root2.title("Admin")
            root2.geometry("1050x650+1+1")
            bg=Label(root2,image=bg_icon).place(x=1,y=1)
            
            l1=Label(root2,text="Log In System",width=30, fg='black', bg='white',font=("arial",22,"bold"))
            l1.place(x=300,y=100)
            l2=Label(root2, text='Enter The Name', compound=LEFT,image=log_img,bd=0,
                       font=('courier', 20, 'bold'),  fg='black', bg='white')
            l2.place(x=120,y=230)
            l3=Label(root2, text='Enter The Password',compound=LEFT,image=pass_img,bd=0,
                       font=('courier', 20, 'bold'),  fg='black', bg='white')
            l3.place(x=120,y=330)
            t1=Entry(root2,bg='white',bd=5,textvariable=adminname,relief=GROOVE,font=("",15))
            t1.place(x=600,y=230)
            t2=Entry(root2,bg='white',bd=5,show='*',textvariable=adminpass,relief=GROOVE,font=("",15))
            t2.place(x=600,y=330)
            b2=Button(root2,text="Ok",bd=5,font=('courier', 20, 'bold'), fg='black', bg='white',command=self.adminaccess)
        #b2.pack()
            b2.place(x=500,y=450)


            

    
    def log_in(self):
            root2=Toplevel(root)
            root2.title("Log In")
            root2.geometry("1050x650+1+1")
            bg=Label(root2,image=bg_icon).place(x=1,y=1)
            l1=Label(root2,text="Log In System",compound=LEFT,  fg='black', bg='white',width=30,font=("arial",22,"bold"))
            l1.place(x=300,y=100)
            #l_img=Label(root2,image=log_img).place(x=100,y=230)
            l2=Label(root2, text=' User Id',compound=LEFT,image=log_img,bd=0,
                       font=('courier', 20, 'bold'), fg='black', bg='white')
            l2.place(x=120,y=230)
            l3=Label(root2, text='Enter The Password',compound=LEFT,image=pass_img,bd=0, 
                       font=('courier', 20, 'bold'),  fg='black', bg='white')
            l3.place(x=120,y=330)
            t1=Entry(root2,bg='white',bd=5,textvariable=uname,relief=GROOVE,font=("",15))
            t1.place(x=600,y=230)
            t2=Entry(root2,bg='white',bd=5,show='*',textvariable=upass,relief=GROOVE,font=("",15))
            t2.place(x=600,y=330)
            b2=Button(root2,text="Ok",font=('courier', 20, 'bold'),  fg='black', bg='white',command=self.useraccess)
        #b2.pack()
            b2.place(x=450,y=450)
    def Register(self):
            root2=Toplevel(root)
            root2.title("Register ")
            root2.geometry("1050x650+1+1")
            bg=Label(root2,image=bg_icon).place(x=1,y=1)
            l1=Label(root2,text="Register Yourself", fg='black', bg='white',width=30,font=("arial",22,"bold"))
            l1.place(x=300,y=100)
            l2=Label(root2, text='Enter The First Name', width=20, height=2,
                       font=('courier', 20, 'bold'),  fg='black', bg='white')
            l2.place(x=120,y=230)
            l3=Label(root2, text='Enter The Second Name', width=20, height=2,
                       font=('courier', 20, 'bold'), fg='black', bg='white')
            l3.place(x=120,y=330)
            l4=Label(root2, text='Enter The Password', width=20, height=2,
                       font=('courier', 20, 'bold'), fg='black', bg='white')
            l4.place(x=120,y=430)
            t4=Entry(root2,bg='white',textvariable=rpass,show='*',bd=5,relief=GROOVE,font=("",15))
            t4.place(x=600,y=430)
            t1=Entry(root2,bg='white', textvariable=rfname,bd=5,relief=GROOVE,font=("",15))
            t1.place(x=600,y=230)
            t2=Entry(root2,bg='white',textvariable=rsname,bd=5,relief=GROOVE,font=("",15))
            t2.place(x=600,y=330)
            b2=Button(root2,text="Submit",width=10,height=2, command=self.save_data,font=('courier', 20, 'bold'), fg='black', bg='white')
            b2.place(x=450,y=550)
    def adminaccess(self):
            if adminname.get()==""or adminpass.get()=="":
                    messagebox.showerror("Error","All fields are required!!")
            if adminname.get()=="suruchi" and adminpass.get()=="123":

                    root2=Toplevel(root)
                    root2.title("Admin Access")
                    root2.geometry("1050x650+1+1")
                    bg=Label(root2,image=bg_icon).place(x=1,y=1)
                    l1=Label(root2, text="Enter The Question",bd=5,
                       font=('courier', 20, 'bold'), fg='black', bg='white').place(x=120,y=230)
                    t1=Entry(root2,bg='white',bd=5,textvariable=AQ,relief=GROOVE,font=("",15))
                    t1.place(x=600,y=230)
                    l2=Label(root2, text="Enter The Answer",bd=5,
                       font=('courier', 20, 'bold'), fg='black', bg='white').place(x=120,y=330)
                    t2=Entry(root2,bg='white',bd=5,textvariable=AA,relief=GROOVE,font=("",15))
                    t2.place(x=600,y=330)
                    b2=Button(root2,text="ADD",font=('courier', 20, 'bold'),bd=5,fg='black', bg='white',command=self.add)
        #b2.pack()  
                    

                    b2.place(x=480,y=450)


                    
            else:
                    messagebox.showerror("Error","Username or password is incorrect")

    def useraccess(self):
            if uname.get()==""or upass.get()=="":
                    messagebox.showerror("Error","All fields are required!!") 
            else:
                    root2=Toplevel(root)
                    root2.title("Register ")
                    root2.geometry("1050x650+1+1")
                    bg=Label(root2,image=bg_icon).place(x=1,y=1)

                    l1=Label(root2,text="Attempt The Question",width=30, fg='black', bg='white',font=("arial",22,"bold"))
                    l1.place(x=300,y=100)
                    l2=Label(root2, text='Question', bd=0,
                       font=('courier', 20, 'bold'),  fg='black', bg='white')
                    l2.place(x=120,y=230)
                    l3=Label(root2, text='Answer',bd=0,
                       font=('courier', 20, 'bold'),  fg='black', bg='white')
                    l3.place(x=120,y=330)
                    l4=Label(root2 ,bd=0,width=25,text=list1,
                    font=('courier', 20, 'bold'),  fg='black', bg='white').place(x=600,y=230)
                    t1=Entry(root2,bg='white',bd=5,textvariable=ans,relief=GROOVE,font=("",15))
                    t1.place(x=600,y=330)
                    
                           
 
        
                    b2=Button(root2,text="SUBMIT",font=('courier', 20, 'bold'),bd=5,fg='black', bg='white',command=self.check)
                    b2.place(x=480,y=450)
                            
                    



    def add(self):
        if(AQ.get()=="") or AA.get()=="":
            messagebox.showinfo("Information","Now Go To The User Panel")

        else:   
            conn=sqlite3.connect("example.db")
            c=conn.cursor()
            #c.execute("CREATE TABLE IF NOT EXISTS Test(S.N. text,question text,answer text)")
            c.execute("Insert into problem VALUES('%s','%s')"%(AQ.get(),AA.get()))
            c.execute("select * from problem")
            print (c.fetchall())
            messagebox.showinfo("Information","Now Go To The User Panel")

            
                         
            
            conn.commit()
            conn.close()
            
            
            '''      
            d.append(list1)
            #d.append(Answer:AA.get())
            print(d);
            '''
            
    def save_data(self):
        if (rfname.get()==""or rsname.get()=="" or rpass.get()==""):
            messagebox.showerror("Error","kindly fill the all detail")
        else:
            conn=sqlite3.connect("answerchecker.db")
            c=conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS Registered_Candidate(First_Name text,Second_Name text,Password text)")
            c.execute("Insert into Registered_Candidate VALUES('%s','%s','%s')"%(rfname.get(),rsname.get(),rpass.get()))
            c.execute("select * from Registered_Candidate")
            print (c.fetchall())
            conn.commit()
            conn.close()
            messagebox.showinfo("Information","Go To Log In Page")

    def check(self):
        print(list2)
        if ans.get()==list2:
            messagebox.showinfo("well done!", "you got 5 out of 5")
        elif(ans.get()==""):
            messagebox.showinfo("oops","you got 0 out 5")
        else:
            messagebox.showinfo("oops","you got 2 out 5")
            
        
            
   

            

global root,bg_icon,log_img,pass_img,adminname,adminpass,AQ,AA,rfname,rsname,rpass,ans
#data={'question':[],'Answer':[]}
#d=pd.DataFrame(data)
root=Tk()
list1=list()
list2=list()
bg_icon=ImageTk.PhotoImage(file="6fee1.jpg")
log_img=PhotoImage(file="user1.png")
pass_img=PhotoImage(file="images1.png")  
uname=StringVar()
upass=StringVar() 
AQ=StringVar()  
AA=StringVar() 
rfname=StringVar()  
rsname=StringVar()
rpass=StringVar()
ans=StringVar()
adminname=StringVar()
adminpass=StringVar()
conn=sqlite3.connect("example.db")
c=conn.cursor()
c.execute("select question from problem")

list1.append(c.fetchone())
print(list1)
c.execute("select answer from problem")
list2.append(c.fetchone())
print(list2)


obj=Answer_checker(root)
#print(d)

root.mainloop()

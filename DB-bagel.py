from tkinter import *
from tkinter import messagebox
import mysql.connector as my

def handle():
    global A,a1,a2,a3
    A=en.get()
    a1=float(p1.get())
    a2=float(p2.get())

    a3=0
    if(s1.get()==1): 
        a3+=0.50
    if(s2.get()==1):  
        a3+=0.25
    if(s3.get()==1):  
        a3+=0.75
    if(s4.get()==1):  
        a3+=0.75
    if(s5.get()==1):  
        a3+=0.75

    a4=a1+a2+a3
    en1.delete(0,END)
    en1.insert(0,a4)

    a5=0.1*a4
    en2.delete(0,END)
    en2.insert(0,a5)

    a6=a4+a5
    en3.delete(0,END)
    en3.insert(0,a6)

    messagebox.showinfo("success!","\nCalculation Successful!")

    db=my.connect(host='localhost',user='root',password='',database='project01')
    cur=db.cursor()
    insert="insert into calc (name,subtot,tax,total) values ('%s',%f,%f,%f)"%(A,a4,a5,a6)

    cur.execute(insert)
    db.commit()
    print("data saved in databases......")

def handle2():
    en1.delete(0,END)
    en2.delete(0,END)
    en3.delete(0,END)
    p1.set(0)  
    p2.set(0) 
    s1.set(0)  
    s2.set(0)  
    s3.set(0) 
    s4.set(0)  
    s5.set(0) 
    messagebox.showinfo("success!","\nReset Successfully!")

def handle3():
    messagebox.showinfo("success!","\nBye, Have a nice day!")
    win.destroy()

win=Tk()

win.title('Bagel and Coffee Price Calculator')
win.geometry('1000x1000')

win.configure(background='#ccffee')

head=Label(text='Heavenly Bagels', font=('broadway',32,'bold'),fg='black',bg='#ccffee')
head.place(x=330,y=5)

a=LabelFrame(text='Good Name?', font=('ariel',25),fg='black',bg='#ccffee',height=120,width=350)
a.place(x=70,y=60)

name=Label(a,text='Enter your Name:',font=('elephant',15),fg='black',bg='#ccffee')
name.place(x=10,y=10)

en=Entry(a,font=('elephant',15),bg='#ccffee',width=15, fg='black')
en.place(x=150,y=10)

a1=LabelFrame(text='Pick a Bagel',fg='black', font=('ariel',25),height=120,width=350,bg='#ccffee')
a1.place(x=70,y=200)

p1=DoubleVar()

r1=Radiobutton(a1,text='White($1.25)',font=('elephant,20'),fg='black',bg='#ccffee',value=1.25,var=p1) 
r1.place(x=10,y=5)
r2=Radiobutton(a1,text='Whole Wheat($1.50)',font=('elephant,20'),fg='black',bg='#ccffee',value=1.50,var=p1) 
r2.place(x=10,y=35)

p2=DoubleVar()

a2=LabelFrame(text='Want Coffee With That?',fg='black', font=('ariel',25),height=250,width=350,bg='#ccffee')
a2.place(x=500,y=60)

r3=Radiobutton(a2,text='None($0.00)',font=('elephant,20'),fg='black',bg='#ccffee',value=0.00,var=p2) 
r3.place(x=10,y=5)
r4=Radiobutton(a2,text='Regular Coffee($1.25)',font=('elephant,20'),fg='black',bg='#ccffee',value=1.25,var=p2)  
r4.place(x=10,y=50)
r5=Radiobutton(a2,text='Cappuccino($2.00)',font=('elephant,20'),fg='black',bg='#ccffee',value=2.00,var=p2)  
r5.place(x=10,y=95)
r6=Radiobutton(a2,text='Cafe au lait($1.75)',font=('elephant,20'),fg='black',bg='#ccffee',value=1.75,var=p2)


a3=LabelFrame(text='Pick Your Toppings',fg='black', font=('ariel',25),height=280,width=350,bg='#ccffee')
a3.place(x=70,y=350)

s1=IntVar()  
c1=Checkbutton(a3,text='Cream Cheese($0.50)',font=('elephant,20'),fg='black',bg='#ccffee',var=s1) 
c1.place(x=10,y=5)
s2=IntVar()  
c2=Checkbutton(a3,text='Butter($0.25)',font=('elephant,20'),fg='black',bg='#ccffee',var=s2)  
s3=IntVar()  
c3=Checkbutton(a3,text='Blueberry Jam($0.75)',font=('elephant,20'),fg='black',bg='#ccffee',var=s3)  
c3.place(x=10,y=95)
s4=IntVar()  
c4=Checkbutton(a3,text='Raspberry($0.75)',font=('elephant,20'),fg='black',bg='#ccffee',var=s4)  
c4.place(x=10,y=140)
s5=IntVar()  
c5=Checkbutton(a3,text='Peach Jelly($0.75)',font=('elephant,20'),fg='black',bg='#ccffee',var=s5)  
c5.place(x=10,y=185)

a4=LabelFrame(text='Price',fg='black', font=('ariel',25),height=280,width=350,bg='#ccffee')
a4.place(x=500,y=350)

subtotal=Label(a4,text='Sub Total:',font=('elephant',20),fg='black',bg='#ccffee')
subtotal.place(x=10,y=10)
en1=Entry(a4,font=('ariel',20),bg='#ccffee', width=10,fg='black')
en1.place(x=110,y=10)

tax=Label(a4,text='Tax:',font=('elephant',20),fg='black',bg='#ccffee')
tax.place(x=10,y=100)
en2=Entry(a4,font=('ariel',20),bg='#ccffee', width=10,fg='black')
en2.place(x=110,y=100)

total=Label(a4,text='Total:',font=('elephant',20),fg='black',bg='#ccffee')
total.place(x=10,y=200)
en3=Entry(a4,font=('ariel',20),bg='#ccffee', width=10,fg='black')
en3.place(x=110,y=200)

btn1=Button(text='Calculate Total',font=('ariel',20),bg='grey',fg='black',width=15,command=handle)  
btn1.place(x=70,y=700)

btn2=Button(text='Reset Form',font=('ariel',20),bg='grey',fg='black',width=12,command=handle2) 
btn2.place(x=380,y=700)

btn3=Button(text='Exit',font=('ariel',20),bg='grey',fg='black',width=7,command=handle3)
btn3.place(x=700,y=700)

win.mainloop()

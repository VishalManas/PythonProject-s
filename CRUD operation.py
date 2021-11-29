from tkinter import *
from tkinter import messagebox
import mysql.connector
data=mysql.connector.connect(host="localhost",user="root",passwd="root",database="vishal")

def insert():
    id=e1.get()
    name=e2.get()
    phno=e3.get()
    if(id=="" or name=="" or phno==""):
        messagebox.showinfo("hello","all fields required")
    else:
        mycursor=data.cursor()
        query="insert into emp values(%s,%s,%s)"
        values=[id,name,phno]
        mycursor.execute(query,values)
        data.commit()
        messagebox.showinfo("hai","insertion success")
def delete():
    id=e1.get()
    mycursor=data.cursor()
    mycursor.execute("delete from emp where eid='"+id+"'")
    data.commit()
    messagebox.showinfo("hai","deletion success")
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

top=Tk()
top.geometry("300x300")
l1=Label(top,text="iD").grid(row=0,column=0)
l2=Label(top,text="name").grid(row=1,column=0)
l3=Label(top,text="phno").grid(row=2,column=0)

e1=Entry(top)
e1.grid(row=0,column=1)
e2=Entry(top)
e2.grid(row=1,column=1)
e3=Entry(top)
e3.grid(row=2,column=1)

b=Button(text="insert",command=insert).grid(row=4,column=1)
b1=Button(text="delete",command=delete).grid(row=4,column=2)
b2=Button(text="clear",command=clear).grid(row=4,column=3)




top.mainloop()

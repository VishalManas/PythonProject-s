from tkinter import *
from tkinter import messagebox
import mysql.connector
data=mysql.connector.connect(host="localhost",user="root",passwd="root",database="sushma")

#1
def insert():
    id=e1.get()
    name=e2.get()
    phno=e3.get()
    if(id=="" or name=="" or phno==""):
        messagebox.showinfo("insert status","all fields are required")
    else:
        mycursor=data.cursor()
        query="insert into emp values(%s,%s,%s)"
        values=[id,name,phno]
        mycursor.execute(query,values)
        data.commit()
        messagebox.showinfo("insert status","success")
def delete():
    id=e1.get()
    if(id==""):
        messagebox.showinfo("delete status","deletion is required")
    else:
        mycursor=data.cursor()
        mycursor.execute("delete from emp where eid=" +id+ "")
        data.commit()
        messagebox.showinfo("deletion success")
def get():
    id=e1.get()
    mycursor=data.cursor()
    mycursor.execute("SELECT*FROM emp where eid=" +id+ "")
    result=mycursor.fetchall()
    for i in result:
        e2.insert(1,i[1])
        e3.insert(1,i[2])
def update():
    id=e1.get()
    name=e2.get()
    phno=e3.get()
    if(id=="" or name=="" or phno==""):
        messagebox.showinfo("update status","all fields are required")
    else:
        mycursor=data.cursor()
        mycursor.execute("update emp set ename='"+name+"',phno='"+phno+"'where eid='"+id+"'")
        data.commit()
        messagebox.showinfo("status","update success")
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

top=Tk()
top.geometry("500x500")
l1=Label(top,text="ID").grid(row=0,column=0)
l2=Label(top,text="Name").grid(row=1,column=0)
l3=Label(top,text="Phno").grid(row=2,column=0)

e1=Entry(top)
e1.grid(row=0,column=1)
e2=Entry(top)
e2.grid(row=1,column=1)
e3=Entry(top)
e3.grid(row=2,column=1)

b1=Button(top,text="insert",command=insert).grid(row=3,column=1)
b2=Button(top,text="delete",command=delete).grid(row=3,column=2)
b3=Button(top,text="update",command=update).grid(row=3,column=3)
b4=Button(top,text="get",command=get).grid(row=3,column=4)

b5=Button(top,text="clear",command=clear).grid(row=3,column=5)
top.mainloop()
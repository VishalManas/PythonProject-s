from tkinter import*
from tkinter import messagebox
import mysql.connector
data=mysql.connector.connect(host="localhost",user="root",passwd="root",database="sushma")

top=Tk()
def std_result():
    sname=e1.get()
    sid=e2.get()
    tel=int(e3.get())
    hin = int(e4.get())
    eng = int(e5.get())
    mat = int(e6.get())
    phy = int(e7.get())
    che = int(e8.get())
    total=tel+hin+eng+mat+phy+che
    avg=int(total/6)
    if(tel>=35 and hin>=35 and eng>=35 and mat>=35 and phy>=35 and che>=35):
        result="pass"
        if(avg>=75):
            grade="A"
        elif(avg>=60 and avg<75):
            grade="B"
        elif(avg>= 50 and avg<60):
            grade = "C"
        else:
            grade="D"
    else:
        result="FAIL"
        grade="NO"
    mycursor=data.cursor()
    query="insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values=[sname,sid,tel,hin,eng,mat,phy,che,total,avg,result,grade]
    mycursor.execute(query,values)
    data.commit()
    messagebox.showinfo("hai","SUCCESS")

def std_clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)

top.geometry("500x500")
l1=Label(top,text="Student Name").grid(row=0,column=0)
l2=Label(top,text="Student ID").grid(row=1,column=0)
l3=Label(top,text="TELUGU").grid(row=2,column=0)
l4=Label(top,text="HINDI").grid(row=3,column=0)
l5=Label(top,text="ENGLISH").grid(row=4,column=0)
l6=Label(top,text="MATHS").grid(row=5,column=0)
l7=Label(top,text="PHYSICS").grid(row=6,column=0)
l8=Label(top,text="CHEMISTRY").grid(row=7,column=0)

e1=Entry(top)
e1.grid(row=0,column=1)
e2=Entry(top)
e2.grid(row=1,column=1)
e3=Entry(top)
e3.grid(row=2,column=1)
e4=Entry(top)
e4.grid(row=3,column=1)
e5=Entry(top)
e5.grid(row=4,column=1)
e6=Entry(top)
e6.grid(row=5,column=1)
e7=Entry(top)
e7.grid(row=6,column=1)
e8=Entry(top)
e8.grid(row=7,column=1)

b=Button(top,text="Result",command=std_result).grid(row=7,column=3)
b1=Button(top,text="Clear",command=std_clear).grid(row=7,column=5)
top.mainloop()



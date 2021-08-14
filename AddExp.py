# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 00:47:05 2020

@author: Siddhesh Dhoke
"""

from tkinter import *
from tkinter import messagebox
import cx_Oracle
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

total_exp = 0       #declaring global variable

class AddExp():
    
    def b1(str):
       
        rootb1 = Tk()
        rootb1.geometry("550x210+570+300")
        rootb1.title("Add Expenses")
        rootb1.configure(background="White")
        
        str11 = StringVar()
        str22 = StringVar()
        
        lbl_name = Label(rootb1, text="NAME: ", bg='yellow', font=("arial", 14)).place(x=50,y=50)
        e11 = Entry(rootb1, textvariable=str11, width=30, fg='black', bg='white', font=("arial", 14))
        e11.place(x=170,y=50)
        
        lbl_amt = Label(rootb1, text='AMOUNT: ', bg='yellow', font=("arial", 14)).place(x=50,y=100)
        e22 = Entry(rootb1, textvariable=str22, width=30, fg='black', bg='white', font=("arial", 14))
        e22.place(x=170,y=100) 
        
        #function for button ok
        def btt1():
            con=None
            try:
                con = cx_Oracle.connect("system/abc123")                        #setting up connection with database
                cursor=con.cursor()
                
                sql = "insert into "+str+" values('%s','%d')"                   #sql query
                args=(e11.get(),int(e22.get()))
                cursor.execute(sql % args)
                
                sql1 = "insert into total1 values('%s','%d')"                    #sql query
                args1=(str, int(e22.get()))
                cursor.execute(sql1 % args1)
                
                sql2 = "select category,total from total where category='"+str+"'"
                cursor.execute(sql2)
                data2 = cursor.fetchall()
                for d in data2:
                    global total_exp
                    total_exp = int(d[1]) + int(e22.get())
                
                sql3 = "update total set total='%d' where category='%s'"
                args3 = (total_exp, str)
                cursor.execute(sql3 % args3)
                                
                con.commit()
                msgg = (cursor.rowcount,"records inserted")
                messagebox.showinfo("Expense",msgg)
                
                """
                fieldnames = ['Category','Amount']
                with open("data.csv", "a") as csvfile:                    
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({"Category":str, "Amount":int(e22.get())})
                """    
            except cx_Oracle.DatabaseError as e:
                con.rollback()
                messagebox.showerror("ERROR",e)
            finally:
                if con is not None:
                    con.close()
       
        btnOk = Button(rootb1, text="OK", font=("arial", 12, "bold"), bg="darkblue", fg="white", command=btt1).place(x=175,y=150)
        btnAddmore = Button(rootb1, text="MORE", font=("arial", 12, "bold"), bg="darkblue", fg="white", command=AddExp.f6).place(x=350,y=150)
        
    def f6():
        root6 = Tk()
        root6.geometry("570x245+570+300")
        root6.title("Add Expenses")
        root6.configure(background="White")
        
        lblCat = Label(root6, text="CATEGORIES", font=("arial", 22, "bold underline"), bg="black", fg="white")
        lblCat.grid(row=0, column=2,pady=10)
        
        #buttons for different categories
        btn1 = Button(root6, text="Medical", font=("arial", 18, "bold"), bg="red", fg="white", width=11, command=lambda: AddExp.b1("medical"))
        btn2 = Button(root6, text="Travel", font=("arial", 18, "bold"), bg="yellow", fg="black", width=11, command=lambda: AddExp.b1("travel"))
        btn3 = Button(root6, text="Education", font=("arial", 18, "bold"), bg="skyblue", fg="black", width=11, command=lambda: AddExp.b1("education"))
        btn4 = Button(root6, text="Rent", font=("arial", 18, "bold"), bg="orange", fg="black", width=11, command=lambda: AddExp.b1("rent"))
        btn5 = Button(root6, text="Groceries", font=("arial", 18, "bold"), bg="lightgreen", fg="black", width=11, command=lambda: AddExp.b1("groceries"))
        btn6 = Button(root6, text="Restaurants", font=("arial", 18, "bold"), bg="red", fg="white", width=11, command=lambda: AddExp.b1("resturants"))
        btn7 = Button(root6, text="Clothing", font=("arial", 18, "bold"), bg="yellow", fg="black", width=11, command=lambda: AddExp.b1("clothing"))
        btn8 = Button(root6, text="Electricity", font=("arial", 18, "bold"), bg="skyblue", fg="black", width=11, command=lambda: AddExp.b1("electricity"))
        btn9 = Button(root6, text="Miscellaneous", font=("arial", 18, "bold"), bg="lightgreen", fg="black", width=11, command=lambda: AddExp.b1("miscellaneous"))
    
        #adding buttons in the window
        btn1.grid(row=1,column=1, padx=5,pady=5)
        btn2.grid(row=1,column=2, padx=5)
        btn3.grid(row=1,column=3, padx=5)
        btn4.grid(row=2,column=1, padx=5,pady=5)
        btn5.grid(row=2,column=2, padx=5)
        btn6.grid(row=2,column=3, padx=5)
        btn7.grid(row=3,column=1, padx=5,pady=5)
        btn8.grid(row=3,column=2, padx=5)
        btn9.grid(row=3,column=3, padx=5)
        root6.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:15:19 2020

@author: Siddhesh Dhoke
"""
import cx_Oracle
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

class ViewExp():
    def f8():
        root = Tk()
        root.title("Expense Tracker")
        root.geometry("450x600+570+160")
        root.configure(background="skyblue")
        root.resizable(False,False)
                
        strr = StringVar()
        lbl_name = Label(root, text="CATEGORY NAME: ", bg='yellow', font=("arial", 14)).place(x=10,y=50)
        e11 = Entry(root, textvariable=strr, width=20, fg='black', bg='white', font=("arial", 14))
        e11.place(x=200,y=50)
        
        #function for ok button
        def okay():
            #conditions for checking if the category entered is correct or not
            if(e11.get()==''):
                messagebox.showerror("Error", "Enter atleast One Category")
                
            elif(e11.get()=='medical' or e11.get()=='travel' or e11.get()=='education' or e11.get()=='rent' or e11.get()=='groceries' or
                 e11.get()=='electricity' or e11.get()=='resturants' or e11.get()=='clothing' or e11.get()=='miscellaneous'):
                
                con=None
                try:
                    con=cx_Oracle.connect("system/abc123")
                    cursor=con.cursor()
                    sql="select name,amount from "+e11.get()
                    cursor.execute(sql)
                    data=cursor.fetchall()
                except cx_Oracle.DatabaseError as e:
                    messagebox.showerror("ERROR",e)
                finally:
                    if con is not None:
                        con.close()

                frm = Frame(root)
                frm.pack(side=tk.LEFT, padx=20)
                tv = ttk.Treeview(frm, columns=(1,2), show="headings", height="15")
                tv.pack()
                tv.heading(1, text="Name")
                tv.heading(2, text="Amount")
                for i in data:
                    tv.insert('', 'end', values=i)
                    
            elif(e11.get()=='total'):                
                con=None
                try:
                    con=cx_Oracle.connect("system/abc123")
                    cursor=con.cursor()
                    sql="select category,total from "+e11.get()
                    cursor.execute(sql)
                    data=cursor.fetchall()
                except cx_Oracle.DatabaseError as e:
                    messagebox.showerror("ERROR",e)
                finally:
                    if con is not None:
                        con.close()

                frm = Frame(root)
                frm.pack(side=tk.LEFT, padx=20)
                tv = ttk.Treeview(frm, columns=(1,2), show="headings", height="15")
                tv.pack()
                tv.heading(1, text="Category")
                tv.heading(2, text="Total")
                for i in data:
                    tv.insert('', 'end', values=i)               
            else:
                messagebox.showerror("Error", "Category does not exists!")   
        #fucntion of i button        
        def info():
            messagebox.showinfo("Category List","1.medical\n2.travel\n3.education\n4.rent\n5.groceries\n6.resturants\n7.clothing\n8.electricity\n9.miscellaneous\n10.total(All Expenses)")

        btnOkay = Button(root, text="OK", font=("arial", 12, "bold"), bg="darkblue", fg="white", command=okay).place(x=175,y=100)
        btnInfo = Button(root, text='i', font=("arial", 14), bg="blue", command=info).place(x=420,y=5)
        
        root.mainloop()
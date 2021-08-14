# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:14:48 2020

@author: Siddhesh Dhoke
"""
from tkinter import *
import cx_Oracle
from tkinter import messagebox

class DelExp():
    def f9():
        root = Tk()
        root.title("Expense Tracker")
        root.geometry("450x400+570+300")
        root.resizable(False,False)
        
        str_1 = StringVar()
        str_2 = StringVar()
        
        lbl_name = Label(root, text="CATEGORY NAME: ", bg='yellow', font=("arial", 14)).place(x=10,y=50)
        e11 = Entry(root, textvariable=str_1, width=20, fg='black', bg='white', font=("arial", 14))
        e11.place(x=200,y=50)
        
        lbl_name = Label(root, text="EXPENSE NAME: ", bg='yellow', font=("arial", 14)).place(x=10,y=100)
        e22 = Entry(root, textvariable=str_2, width=20, fg='black', bg='white', font=("arial", 14))
        e22.place(x=200,y=100)
        
        #function defination for OK button
        def okay():
            
            if(e11.get()==''):
                messagebox.showerror("Error", "Enter atleast One Category")
            elif(e11.get()=='medical' or e11.get()=='travel' or e11.get()=='education' or e11.get()=='rent' or e11.get()=='groceries' or
                 e11.get()=='electricity' or e11.get()=='resturants' or e11.get()=='clothing' or e11.get()=='miscellaneous'):
                
                con=None
                try:
                    con=cx_Oracle.connect("system/abc123")
                    cursor=con.cursor()
                    #rno=int(input("enter rno "))
                    sql="delete from "+e11.get()+" where name='%s'"
                    args=(e22.get())
                    cursor.execute(sql % args)
                    con.commit()
                    msgg = (cursor.rowcount,"row deleted")
                    messagebox.showinfo("Delete Expense",msgg)
                    #print(cursor.rowcount,"row deleted")
                except cx_Oracle.DatabaseError as e:
                    print("issue",e)
                finally:
                    if con is not None:
                        con.close()
            else:
                messagebox.showerror("Error", "Category does not exists")  
        
        #function defination for DELETE ALL button        
        def delAll():
            
            if(e11.get()==''):
                messagebox.showerror("Error", "Enter atleast One Category")
            elif(e11.get()=='medical' or e11.get()=='travel' or e11.get()=='education' or e11.get()=='rent' or e11.get()=='groceries' or
                 e11.get()=='electricity' or e11.get()=='resturants' or e11.get()=='clothing' or e11.get()=='miscellaneous'):
                
                con=None
                try:
                    con=cx_Oracle.connect("system/abc123")
                    cursor=con.cursor()
                    sql="delete from "+e11.get()
                    sql11 = "update total set total='0' where category='"+e11.get()+"'"
                    cursor.execute(sql)
                    cursor.execute(sql11)
                    con.commit()
                    messagebox.showinfo("Delete Expense","Data from "+e11.get()+" is DELETED!")
                except cx_Oracle.DatabaseError as e:
                    print("issue",e)
                finally:
                    if con is not None:
                        con.close()
            else:
                messagebox.showerror("Error", "Category does not exists") 
        
        #function defination for RESET button
        def reset():
            try:
                con=cx_Oracle.connect("system/abc123")
                cursor=con.cursor()
                #sql queries to delete data from all categories
                sql1="delete from medical"
                sql2="delete from travel"
                sql3="delete from education"
                sql4="delete from rent"
                sql5="delete from groceries"
                sql6="delete from resturants"
                sql7="delete from clothing"
                sql8="delete from electricity"
                sql9="delete from miscellaneous"
                
                cursor.execute(sql1)
                cursor.execute(sql2)
                cursor.execute(sql3)
                cursor.execute(sql4)
                cursor.execute(sql5)
                cursor.execute(sql6)
                cursor.execute(sql7)
                cursor.execute(sql8)
                cursor.execute(sql9)
                
                sql10="update total set total='0'"
                cursor.execute(sql10)
                
                
                con.commit()
                messagebox.showinfo("Delete Expense","Data from all categories is DELETED!")
            except cx_Oracle.DatabaseError as e:
                messagebox.showerror("ERROR",e)
            finally:
                if con is not None:
                    con.close()
            

        btnOkay = Button(root, text="OK", font=("arial", 12, "bold"),width=10, bg="darkblue", fg="white", command=okay).place(x=175,y=150)
        btnDelAll = Button(root, text="DELETE ALL", font=("arial", 12, "bold"),width=10, bg="darkblue", fg="white", command=delAll).place(x=100,y=250)
        btnReset = Button(root, text="RESET", font=("arial", 12, "bold"),width=10, bg="darkblue", fg="white", command=reset).place(x=250,y=250)
        
        lblNote = Label(root, text="DELETE ALL button deletes all data from a given category\nRESET button delete data from all category", font=("arial",12), bg="red", fg="white").place(x=20,y=300)
        
        root.mainloop()
    
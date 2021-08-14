# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:47:07 2020

@author: Siddhesh Dhoke

"""
#imports needed
from tkinter import *
from tkinter import messagebox
from main import *
from PIL import ImageTk, Image


root = Tk()                             #root window for gui
root.title("Expense Tracker")           #title for gui window
root.geometry("400x200+570+300")
root.configure(background="skyblue")
root.resizable(False,False)

#messagebox.showinfo("WELCOME","WELCOME TO EXPENSE TRACKER")

lbl_user = Label(root, text="USERNAME ", bg='yellow').place(x=50,y=50)          #label for username
str1 = StringVar()
e1 = Entry(root, textvariable=str1, width=30, fg='black', bg='white')           #entry for taking username input
e1.place(x=150,y=50)                                                            #placing the entry in window

lbl_pass = Label(root, text='PASSWORD ', bg='yellow').place(x=50,y=100)         #label for password
str2 = StringVar()
e2 = Entry(root, width=30, fg='black', bg='white', show='*')                    #entry for taking password input
e2.place(x=150,y=100)                           
        
def f1():
    s1 = e1.get()
    s2 = e2.get()
    if (s1=="sid" and s2=="1234"):
        f3()
    elif (s1=="anviksha" and s2=="1234"):
        f3()
    elif (s1=="neer" and s2=="1234"):
        f3()
    elif (s1=="dion" and s2=="1234"):
        f3()
    else:
        messagebox.showerror("Error", "Incorrect Username or Password")
        
        
b = Button(root, width=15, text='Login', bg='darkblue', fg='white',command=f1).place(x=130,y=160)

root.mainloop()                                                                 #closing the root window
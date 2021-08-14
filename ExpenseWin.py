# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 00:40:53 2020

@author: Siddhesh Dhoke
"""

from tkinter import *
from AddExp import *
from ChkExp import *
from ViewExp import *
from DelExp import *
from main import *

def f3():
  
    root3 = Tk()
    root3.geometry("420x400+570+300")
    root3.title("Expenses")
    root3.configure(background="Sky Blue")
    
    btnChk = Button(root3, text="CHECK EXPENSES", font=("arial", 22, "bold"), bg="yellow",width=17, command=ChkExp.f7)      #btn for checking expenses
    btnAdd = Button(root3, text="ADD EXPENSES", font=("arial", 22, "bold"), bg="yellow",width=17,command=AddExp.f6)         #btn for adding expenses
    btnView = Button(root3, text="VIEW EXPENSES", font=("arial", 22, "bold"), bg="yellow",width=17,command=ViewExp.f8)      #btn for viewing expenses
    btnDel = Button(root3, text="DELETE EXPENSES", font=("arial", 22, "bold"), bg="yellow",width=17,command=DelExp.f9)      #btn for deleting expenses
    
    btnAdd.grid(padx=65, pady=20)
    btnChk.grid(padx=65, pady=20)
    btnView.grid(padx=65, pady=20)
    btnDel.grid(padx=65, pady=20)
   
    root3.mainloop()
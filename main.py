# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:05:04 2020

@author: Siddhesh Dhoke
"""
from tkinter import *
from ExpenseWin import *
from SavingWin import *
class main():
    
    def f2():
        root2 = Tk()
        root2.geometry("400x300+570+300")
        root2.title("Expense Tracker")
        root2.configure(background='sky blue')

        btnExp = Button(root2, text="EXPENSES", font=("arial", 22, "bold underline"), bg="red",command=f3)
        btnExp.grid(pady=60, padx=110)
        
        root2.mainloop()
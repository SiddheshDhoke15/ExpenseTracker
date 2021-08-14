# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:45:53 2020

@author: Siddhesh Dhoke
"""

from tkinter import *
from tkinter import messagebox
import cx_Oracle
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class ChkExp():
    def f7():
        con = None
        try:
            con = cx_Oracle.connect("system/abc123")        #setting up connection with database
            cursor=con.cursor()
            
            cat = []                                        #list to append category
            tot = []                                        #list to append total of each category
            
            sql4 = "select category,total from total"       #sql query
            cursor.execute(sql4)
            data4 = cursor.fetchall()
            
            for row in data4:
                cat.append(row[0])
                tot.append(row[1])
                
            plt.figure(figsize=(7,5))
            plt.pie(tot, labels=cat,explode=[0,0,0,0,0,0,0,0,0],shadow=True,autopct='%.2f%%')
            plt.grid()
            plt.show()                                      #to see pie chart
            
            con.commit()
        except cx_Oracle.DatabaseError as e:
            con.rollback()
            messagebox.showerror("ERROR",e)
        finally:
            if con is not None:
                con.close()

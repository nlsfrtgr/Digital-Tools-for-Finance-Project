#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:41:12 2021

@author: antoine
"""

import measure as ms
import portfolio as pf
import os 
import pandas as pd 
import matplotlib.pyplot as plt

path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
path+= "/data/stock_prices.csv"

df = pd.read_csv(path, sep = ",", decimal = ".", encoding='latin-1')
df["Date"] = pd.to_datetime(df["Date"], format = "%Y/%m/%d")
df.set_index("Date",inplace = True)





def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
createFolder('./output/')

path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
path+= "/output/"



plt.style.use('seaborn')
fig = plt.figure(figsize=(12, 8), dpi=120)


plt.plot(df["AAPL"], color = 'olivedrab', label = "AAPL")
plt.plot(df["INTC"], color = 'navy', label = "INTC")
plt.plot(df["F"], color = 'maroon', label = "F")
plt.plot(df["PFE"], color = 'deeppink', label = "PFE")
plt.plot(df["T"], color = 'cadetblue', label = "T")
plt.xlabel("Dates")
plt.ylabel('Prices')

plt.title("Stocks prices",  weight='bold')

plt.legend()

plt.grid(True)

plt.tight_layout()
plt.show()
fig.savefig('output/price')



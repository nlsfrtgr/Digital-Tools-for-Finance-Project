#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 11:38:41 2021

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


df_returns, df_monthly_returns = get_return(df)


table_return = ms.get_tabel(df_returns)

table_return_monthly = ms.get_tabel(df_monthly_returns)



correlation = df_returns.corr()




w = pf.get_weights(df_returns)

ret = pf.portfolio_return(w,df_returns.T)



plt.figure(figsize = (8, 8))
x = w
plt.pie(x, labels = df.columns,
           colors = ['olivedrab', 'royalblue', 'maroon',"deeppink","cadetblue"],
           autopct = lambda x: str(round(x, 2)) + '%',
           pctdistance = 0.7, labeldistance = 1.2,
           shadow = True)
plt.tight_layout()
plt.savefig('output/weights.png')
plt.show()





plt.style.use('seaborn')
fig = plt.figure(figsize=(12, 8), dpi=120)
plt.plot((1+ret).cumprod(), color = 'cadetblue')
plt.xlabel("Dates")
plt.ylabel('Performance')

plt.title("Performance of the portfolio")

plt.grid(True)

plt.tight_layout()
plt.show()
fig.savefig('output/performance')
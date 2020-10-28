# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:36:40 2020

@author: SchmittyCodes
"""

from scipy import stats
import pandas as pd
import yahoo_fin.stock_info as si
from yahoo_fin.stock_info import get_data
from IPython.display import display
import statistics
import numpy as np

reg = {}
diff = []
stdevdf = []
nets = []
netdf = {}

def ticksfunc():
    return pd.read_csv(r"C:\Users\schmi\OneDrive\Documents\ticks.csv", index_col = 0)

ticks = ticksfunc()

for k in range(5):
    
    tick = ticks.at[k,"tick"]
    daily= get_data(tick, start_date="10/09/2019", end_date="10/08/2020", index_as_date = False, interval="1d")

    x = []
    y = []
    changelist = []

    for j in range(252):
        x.append(j)
        j =+1



    for i in range(252):
    
        close = daily.at[i,"adjclose"]
        y.append(close)
        for i in range(251):
            close1 = daily.at[i,"adjclose"]
            close2 = daily.at[i+1,"adjclose"]
            change = (close2 -close1) / close1
            changelist.append(change)
          

    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def myfunc(x):
        return slope * x + intercept

    mymodel = list(map(myfunc, x))



    current = si.get_live_price(tick)

    predict = slope * 252 + intercept

    diff = (current - predict) / predict


    mean = statistics.mean(changelist)
#    stdev = statistics.stdev(changelist)
#    reg[tick] = diff
#    stdevdf[tick] = stdev
    netdf[tick] = mean

    means = nets.append(mean)
    reg['Daily Net'] = mean


    print(tick, "{0:.2%}".format(k / 202))
    
    

display(netdf) 
f = open(r"C:\Users\schmi\Downloads\1yearreg.txt", "w")
f.write(str(netdf))
f.close()



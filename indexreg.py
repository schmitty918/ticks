# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:36:40 2020

@author: schmi
"""

import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import yahoo_fin.stock_info as si
from yahoo_fin.stock_info import get_data
from datetime import datetime, timedelta

reg = {}
index = ['^DJI','^IXIC', '^GSPC']


for k in index:
    
    
    old = datetime.today() - timedelta(365)

    daily= get_data(k, start_date=old, end_date=datetime.today(), index_as_date = False, interval="1d")

    x = []
    y = []

    for j in range(251):
        x.append(j)
        j =+1



    for i in range(251):
    
        close = daily.at[i,"adjclose"]
        y.append(close)

    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def myfunc(x):
        return slope * x + intercept

    mymodel = list(map(myfunc, x))

    plt.scatter(x, y)
    plt.plot(x, mymodel)
    plt.show()

    current = si.get_live_price(k)

    predict = slope * 252 + intercept

    diff = (current - predict) / predict

    print("the predicted price of",  k, " for today using one year of price history is" , round(predict,2))

    print("the current price today is" , round(current,2))

    print("the differences is", "{0:.0%}".format(diff) )
    
    reg[k] = "{0:.0%}".format(diff)
    
    old = datetime.today() - timedelta(185)

    daily= get_data(k, start_date=old, end_date=datetime.today(), index_as_date = False, interval="1d")

    x = []
    y = []

    for j in range(126):
        x.append(j)
        j =+1



    for i in range(126):
    
        close = daily.at[i,"adjclose"]
        y.append(close)

    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def myfunc(x):
        return slope * x + intercept

    mymodel = list(map(myfunc, x))

    plt.scatter(x, y)
    plt.plot(x, mymodel)
    plt.show()

    current = si.get_live_price(k)

    predict = slope * 126 + intercept

    diff = (current - predict) / predict

    print("the predicted price of",  k, " for today using one year of price history is" , round(predict,2))

    print("the current price today is" , round(current,2))

    print("the differences is", "{0:.0%}".format(diff) )
    
    reg[k] = "{0:.0%}".format(diff)    
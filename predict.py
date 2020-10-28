# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:46:35 2020

@author: schmi
"""

import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import yahoo_fin.stock_info as si
from yahoo_fin.stock_info import get_data
from datetime import datetime, timedelta
import statistics

tick = '^DJI'

daily= get_data(tick, start_date='10/25/2010', end_date=datetime.today(), index_as_date = False, interval="1d")

x = []
y = []
predict = []


rangeindex = 252*10


    
for i in range(2519):

    close = daily.at[i,"adjclose"]
    y.append(close)    
    
current = si.get_live_price(tick)

j = 0

for j in range(2517):
    n0 = y[j]
    n1 = y[j+1]
    change = (n1 - n0) / n0
    if change < -0.02:
        n2 = y[j+2]
        change2 = (n2 - n1) / n1
        predict.append(change2)
        
mean = statistics.mean(predict)
print(mean)
    
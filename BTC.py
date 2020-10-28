# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:55:57 2020

@author: schmi
"""

from scipy import stats
import pandas as pd
import yahoo_fin.stock_info as si
from yahoo_fin.stock_info import get_data
from IPython.display import display
import statistics
import time
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import winsound
from pygame import mixer  # Load the popular external library
import time

mixer.init()
mixer.music.load(r"C:\Users\schmi\Downloads\download\Super Mario Bros. medley.mp3")

index = "^DJI"
#index = "BTC-USD"

x_index = []
y_index = []
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second



now = datetime.now()
current_time = now.strftime("%H:%M:%S")

opentime = '09:30:00'
closetime = '18:00:00'
goal = 13200

i = 0
#for i in range(100000):
while i < 2:



    current = si.get_live_price(index)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    x_index.append(current_time)
    y_index.append(current)
    plt.plot(x_index,y_index)
    plt.show()


    if current > goal:
        mixer.music.play()
        time.sleep(5)
        mixer.music.stop()
            

           
           
print("offline " , i)
time.sleep(10)

 
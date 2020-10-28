# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:16:54 2020

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
from pygame import mixer  # Load the popular external library
from twilio.rest import Client
from datetime import datetime, timedelta
import random
import sys

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACba1bf78fcb42907f6a202e715cf47f5d", "042b912a1072faadb019f386da63a2a8")



#variables
wake = '07:30:00'
analysis = '14:10:00'
analysisclose = '22:10:00'
gmflag = 0
t = 0
yrflag = 0
halfflag = 0
command = ''
yrnetflag = 0
halfnetflag = 0
halfsdflag = 0
yrsdflag = 0
opentime = '09:30:00'
closetime = '16:00:00'
index = "^dji"
#index = "^IXIC"
x_index = []
y_index = []
openflag = 0
nightflag = 0
five = 0.05
bar = 0
dot = 0

#TIMER
while t < 2:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    command = input("What would you like SchmittyBot to do? \n Choice:")
    print("Beep Boop, SchmittyBot will now perform" + command)
  
#CASS WAKEUP    
    if current_time > wake and current_time < '07:35:00' and gmflag == 0:
        
    

        message = client.messages \
                .create(
                     body="SchmittyBot says Too early go back to sleep shawty beep boop",
                     from_='+19033073965',
                     to='+12705905412'
                 )

        print(message.sid)
        print('good morning sent')
        gmflag += 1
    if current_time > '7:35:00' and current_time < '7:40:00':
        flag = 0
    if current_time > '09:30:00' and current_time < '09:35:00' and openflag == 0:
        mixer.init()
        mixer.music.load(r"C:\Users\schmi\OneDrive\Documents\audio\itsme.mp3")
        mixer.music.play()
        openflag += 1
        print('mario open')
    #1YEAR REG
    if command == 'run analysis' and yrflag == 0:
        print('starting 1 year reg')
     
        mixer.init()
        mixer.music.load(r"C:\Users\schmi\Downloads\analysis.mp3")
        
        
        
        
        mixer.music.play()
        
        
        time.sleep(5)
        mixer.init()
        
        mixer.music.load(r"C:\Users\schmi\Downloads\oneyearreg.mp3")       
        mixer.music.play()  
       
        reg = {}
        diff = []
        stdevdf = []
        nets = []
        l = 0
        five = 0.01
    
        url = 'https://raw.githubusercontent.com/schmitty918/ticks/main/ticks.csv'
        ticks = pd.read_csv(url, error_bad_lines=False)
        old = datetime.today() - timedelta(367)
    
        for k in range(479):
            sys.stdout.write('\r')
            percent = k / 477
            if percent > five:
                l += 1
                five = five + .01
           # the exact output you're looking for:
            sys.stdout.write("[%-100s] %d%%" % ('='*l, l))
            sys.stdout.flush()


        
            tick = ticks.at[k,"tick"]
            daily= get_data(tick, start_date=old, end_date=datetime.today(), index_as_date = False, interval="1d")
    
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
            reg[tick] = diff
        #    stdevdf[tick] = stdev
        #    netdf[tick] = mean
        
            means = nets.append(mean)
           # reg['Daily Net'] = mean
        
        
          #  print(tick, "{0:.2%}".format(k / 477))
            
            
        
        #display(reg) 
        f = open(r"C:\Users\schmi\Downloads\1yearreg.txt", "w")
        f.write(str(reg))
        f.close()
        yrflag += 1
        print('one year reg finished')
    #6 MONTH REG
    if command == 'run analysis' and halfflag == 0:
        print('starting 6 month reg')
        reg = {}
        diff = []
        stdevdf = []
        nets = []
        l = 0
        five = 0.05
    
        url = 'https://raw.githubusercontent.com/schmitty918/ticks/main/ticks.csv'
        ticks = pd.read_csv(url, error_bad_lines=False)
        old = datetime.today() - timedelta(367)
    
        for k in range(479):
            sys.stdout.write('\r')
            percent = k / 477
            if percent > five:
                l += 1
                five = five + .01
           # the exact output you're looking for:
            sys.stdout.write("[%-100s] %d%%" % ('='*l, l))
            sys.stdout.flush()
        
            tick = ticks.at[k,"tick"]
            daily= get_data(tick, start_date=old, end_date=datetime.today(), index_as_date = False, interval="1d")
    
            x = []
            y = []
            changelist = []
            
        
            for j in range(126):
                x.append(j)
                j =+1
        
        
        
            for i in range(126):
            
                close = daily.at[i,"adjclose"]
                y.append(close)
                for i in range(125):
                    close1 = daily.at[i,"adjclose"]
                    close2 = daily.at[i+1,"adjclose"]
                    change = (close2 -close1) / close1
                    changelist.append(change)
                  
        
            slope, intercept, r, p, std_err = stats.linregress(x, y)
        
            def myfunc(x):
                return slope * x + intercept
        
            mymodel = list(map(myfunc, x))
        
        
        
            current = si.get_live_price(tick)
        
            predict = slope * 126 + intercept
        
            diff = (current - predict) / predict
        
        
            mean = statistics.mean(changelist)
        #    stdev = statistics.stdev(changelist)
            reg[tick] = diff
        #    stdevdf[tick] = stdev
        #    netdf[tick] = mean
        
            means = nets.append(mean)
           # reg['Daily Net'] = mean
        
        
        #    print(tick, "{0:.2%}".format(k / 477))
            
            
        
       # display(reg) 
        f = open(r"C:\Users\schmi\Downloads\6monthreg.txt", "w")
        f.write(str(reg))
        f.close()
        halfflag += 1
        print('6 month reg finished')
    #1 YEAR NET
    if command == 'run analysis' and yrnetflag == 0:
        print('starting 1 year net')
        reg = {}
        diff = []
        stdevdf = []
        nets = []
        netdf = {}
        l = 0
        five = 0.05
    
        url = 'https://raw.githubusercontent.com/schmitty918/ticks/main/ticks.csv'
        ticks = pd.read_csv(url, error_bad_lines=False)
        old = datetime.today() - timedelta(367)
    
        for k in range(479):
            sys.stdout.write('\r')
            percent = k / 477
            if percent > five:
                l += 1
                five = five + .01
           # the exact output you're looking for:
            sys.stdout.write("[%-100s] %d%%" % ('='*l, l))
            sys.stdout.flush()
        
            tick = ticks.at[k,"tick"]
            daily= get_data(tick, start_date=old, end_date=datetime.today(), index_as_date = False, interval="1d")
    
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
        
        
          #  print(tick, "{0:.2%}".format(k / 477))
            
            
        

        f = open(r"C:\Users\schmi\Downloads\1yearnet.txt", "w")
        f.write(str(netdf))
        f.close()
        yrnetflag += 1    
        print('1 year net finished')
    #6 MONTH NET
    if command == 'run analysis' and halfnetflag == 0:
        print('starting 6 month net')
        reg = {}
        diff = []
        stdevdf = []
        nets = []
        netdf = {}
        l = 0
        five = 0.05
    
        url = 'https://raw.githubusercontent.com/schmitty918/ticks/main/ticks.csv'
        ticks = pd.read_csv(url, error_bad_lines=False)
        old = datetime.today() - timedelta(367)
    
        for k in range(479):
            sys.stdout.write('\r')
            percent = k / 477
            if percent > five:
                l += 1
                five = five + .01
           # the exact output you're looking for:
            sys.stdout.write("[%-100s] %d%%" % ('='*l, l))
            sys.stdout.flush()
        
            tick = ticks.at[k,"tick"]
            daily= get_data(tick, start_date=old, end_date=datetime.today(), index_as_date = False, interval="1d")
    
            x = []
            y = []
            changelist = []
            
        
            for j in range(126):
                x.append(j)
                j =+1
        
        
        
            for i in range(126):
            
                close = daily.at[i,"adjclose"]
                y.append(close)
                for i in range(125):
                    close1 = daily.at[i,"adjclose"]
                    close2 = daily.at[i+1,"adjclose"]
                    change = (close2 -close1) / close1
                    changelist.append(change)
                  
        
            slope, intercept, r, p, std_err = stats.linregress(x, y)
        
            def myfunc(x):
                return slope * x + intercept
        
            mymodel = list(map(myfunc, x))
        
        
        
            current = si.get_live_price(tick)
        
            predict = slope * 126 + intercept
        
            diff = (current - predict) / predict
        
        
            mean = statistics.mean(changelist)
        #    stdev = statistics.stdev(changelist)
        #   reg[tick] = diff
        #    stdevdf[tick] = stdev
            netdf[tick] = mean
        
            means = nets.append(mean)
           # reg['Daily Net'] = mean
        
        
          #  print(tick, "{0:.2%}".format(k / 477))
            
            
        

        f = open(r"C:\Users\schmi\Downloads\6monthnet.txt", "w")
        f.write(str(netdf))
        f.close()
        halfnetflag += 1  
        print('6 month net finished')
     # 1 YEAR SD   
    if command == 'run analysis' and yrsdflag == 0:
        print('starting 1 year standard deviation')
        reg = {}
        diff = []
        stdevdf = []
        nets = []
        netdf = {}
        sddf = {}
        l = 0
        five = 0.05
    
        url = 'https://raw.githubusercontent.com/schmitty918/ticks/main/ticks.csv'
        ticks = pd.read_csv(url, error_bad_lines=False)
        old = datetime.today() - timedelta(367)
    
        for k in range(479):
            sys.stdout.write('\r')
            percent = k / 477
            if percent > five:
                l += 1
                five = five + .01
           # the exact output you're looking for:
            sys.stdout.write("[%-100s] %d%%" % ('='*l, l))
            sys.stdout.flush()
        
            tick = ticks.at[k,"tick"]
            daily= get_data(tick, start_date=old, end_date=datetime.today(), index_as_date = False, interval="1d")
    
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
        
        
         #   mean = statistics.mean(changelist)
            stdev = statistics.stdev(changelist)
        #    reg[tick] = diff
        #    stdevdf[tick] = stdev
         #   netdf[tick] = mean
            sddf[tick] = stdev
        
           # means = nets.append(mean)
           #reg['Daily Net'] = mean
        
        
         #   print(tick, "{0:.2%}".format(k / 477))
            
            
        

        f = open(r"C:\Users\schmi\Downloads\1yearsd.txt", "w")
        f.write(str(sddf))
        f.close()
        yrsdflag += 1     
        print('1 year SD finshed')
    # 6 MONTH SD
    if command == 'run analysis' and halfsdflag == 0:
        print('starting 6 month standard deviation')
        reg = {}
        diff = []
        stdevdf = []
        nets = []
        netdf = {}
        sddf = {}
        l = 0
        five = 0.05
    
        url = 'https://raw.githubusercontent.com/schmitty918/ticks/main/ticks.csv'
        ticks = pd.read_csv(url, error_bad_lines=False)
        old = datetime.today() - timedelta(367)
    
        for k in range(479):
            sys.stdout.write('\r')
            percent = k / 477
            if percent > five:
                l += 1
                five = five + .01
           # the exact output you're looking for:
            sys.stdout.write("[%-100s] %d%%" % ('='*l, l))
            sys.stdout.flush()
        
            tick = ticks.at[k,"tick"]
            daily= get_data(tick, start_date=old, end_date=datetime.today(), index_as_date = False, interval="1d")
    
            x = []
            y = []
            changelist = []
            
        
            for j in range(126):
                x.append(j)
                j =+1
        
        
        
            for i in range(126):
            
                close = daily.at[i,"adjclose"]
                y.append(close)
                for i in range(125):
                    close1 = daily.at[i,"adjclose"]
                    close2 = daily.at[i+1,"adjclose"]
                    change = (close2 -close1) / close1
                    changelist.append(change)
                  
        
            slope, intercept, r, p, std_err = stats.linregress(x, y)
        
            def myfunc(x):
                return slope * x + intercept
        
            mymodel = list(map(myfunc, x))
        
        
        
            current = si.get_live_price(tick)
        
            predict = slope * 126 + intercept
        
            diff = (current - predict) / predict
        
        
          #  mean = statistics.mean(changelist)
            stdev = statistics.stdev(changelist)
        #   reg[tick] = diff
        #    stdevdf[tick] = stdev
        #    netdf[tick] = mean
            sddf[tick] = stdev
        
        #    means = nets.append(mean)
        #    reg['Daily Net'] = mean
        
        
            #print(tick, "{0:.2%}".format(k / 477))
            
            
        

        f = open(r"C:\Users\schmi\Downloads\6monthstdev.txt", "w")
        f.write(str(sddf))
        f.close()
        halfsdflag += 1     
        print('6 month SD finished')
    #flag reset
    if current_time > '9:35:00' and current_time < '9:40:00':
        yrflag = 0
        halfflag = 0
        yrnetflag = 0
        halfnetflag = 0
        halfsdflag = 0
        yrsdflag = 0


    #market open flag reset
    if current_time > '9:35:30' and current_time < '9:40:00' and openflag == 1:
        openflag = 0    
    #index
    if current_time > opentime and current_time < closetime:
        current = si.get_live_price(index)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        x_index.append(current_time)
        y_index.append(current)
        plt.plot(x_index,y_index)
        plt.show()
        time.sleep(10)    
    if current_time > '00:08:00' and current_time < '00:10:00' and nightflag == 0:
        rand = random.randint(1,8)
        if rand == 1:
            text = "beautiful"
        if rand == 2:
            text = "wonderful"
        if rand == 3:
            text = "splended"    
        if rand == 4:
            text = "brilliant"
        if rand == 5:
            text = "sexy"
        if rand == 6:
            text = "pretty"
        if rand == 7:
            text = "favorite"    
        if rand == 8:
            text = "best"
        
        text = ('Sweet Dream My ' + text + ' girl.  Wut dem legs do?')        
                
        message = client.messages \
            .create(
                         body= text,
                            from_='+19033073965',
                            to='+12705905412'
                     )
        
        print(message.sid)
        print('good night message sent')
        nightflag += 1
        
   
    #CLOCK MANAGEMENT
    time.sleep(2) 
    sys.stdout.write('\r')
    percent = t / 477
    if percent > five:
        bar += 1
        five = five + .05
    if dot < 4:
        dot += 1
    else:
        dot = 0
         
    # the exact output you're looking for:
    sys.stdout.write("[%-12s] %d%%" %  ('Working' + '.' * dot, 5*t))
    sys.stdout.flush()

        


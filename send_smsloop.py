# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 19:55:15 2020

@author: schmi
"""

# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
import random
import time

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACba1bf78fcb42907f6a202e715cf47f5d", "042b912a1072faadb019f386da63a2a8")

for x in range(10):

    rand = random.randint(1,8)
    if rand == 1:
        text = "You are cute"
    if rand == 2:
        text = "I like you"
    if rand == 3:
        text = "falling in love"    
    if rand == 4:
        text = "You are mine"
    if rand == 5:
        text = "You are the best"
    if rand == 6:
        text = "You are brilliant"
    if rand == 7:
        text = "You are glamorous"    
    if rand == 8:
        text = "You are my queen"        
        
    message = client.messages \
        .create(
                     body= text,
                        from_='+19033073965',
                        to='+12705905412'
                 )

    print(message.sid)
    print(rand)
    time.sleep(2)
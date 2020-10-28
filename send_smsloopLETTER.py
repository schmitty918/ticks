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

for x in "ILIKEYOUMORE":

    text = x     
        
    message = client.messages \
        .create(
                     body= text,
                        from_='+19033073965',
                        to='+12705905412'
                 )

    print(message.sid)

    time.sleep(2)
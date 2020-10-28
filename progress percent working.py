# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:42:16 2020

@author: schmi
"""

from time import sleep
import sys
five = 0.05
bar = 0
dot = 0
for i in range(202):
    sys.stdout.write('\r')
    percent = i / 202
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
    sleep(0.25)
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:49:19 2020

@author: schmi
"""


from pygame import mixer  # Load the popular external library
import time




mixer.init()
mixer.music.load(r"C:\Users\schmi\Downloads\analysis.mp3")




mixer.music.play()


time.sleep(10)
mixer.init()

mixer.music.load(r"C:\Users\schmi\Downloads\oneyearreg.mp3")       
mixer.music.play()  






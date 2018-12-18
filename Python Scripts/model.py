# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 09:40:10 2018

@author: ml17kfma
 """
#hello Khalaf Alrowily
y0 = 57
x0 = 57
print ("x0", x0)
print ("y0", y0)
y1 = 90
x1 = 90 
print ("y1", y1)
print ("x1", x1)
import random
random_number = random.random()
print ("random_number", random_number)

if random_number < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print (y0)
if random_number < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print (x0)

#move x, y randomly to change values

dist = (((y0 - y1)**2 + (x0 - x1)**2)**0.5)
print (dist)


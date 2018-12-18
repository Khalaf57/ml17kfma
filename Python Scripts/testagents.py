# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:42:00 2018

@author: ml17kfma
"""
import random 
#y0 = random.randint (0,99)
#x0 = random.randint (0,99)
agents = []
number_of_agents = 50

for i in range(number_of_agents):
    agents.append ([random.randint (0,99),random.randint (0,99)])
    #print (i)
print( agents[0][0] )
print( agents[0][1] )    
#print (max (agents))


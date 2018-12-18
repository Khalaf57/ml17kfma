# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:31:00 2018

@author: ml17kfma
"""
import random
# agentframework.py

class Agent():
    
    def __init__(self):
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
        pass 
    
    def move(self):
        #print("moving")
        if random.random() < 0.5:
            #print("increase y")
            self.y = (self.y + 1) % 100
        else:
            #print("decrease y")
            self.y = (self.y - 1) % 100
        if random.random() < 0.5:
            #print("increase x")
            self.x = (self.x + 1) % 100
        else:
            #print("decrease x")
            self.x = (self.x - 1) % 100
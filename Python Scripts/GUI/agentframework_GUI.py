# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:31:00 2018

@author: ml17kfma
"""
import random
# agentframework.py

class Agent():
    
    def __init__(self, name, environment, randomSeed, probabilityMove, printlevel):
        random.seed(randomSeed)
        self.x = random.randint(0, 299)
        self.y = random.randint(0, 299)
        self.name = name
        self.environment = environment
        self.store = 0
        self.probabilityMove = probabilityMove
        self.printlevel = printlevel
        pass
    
    def __str__(self):
        return "Agent " + str(self.name) + ": Location x=" + str(self.x) + "; y=" + str(self.y) + " Store=" + str(self.store)
 
    # describ the movement ability of agents whether they move or stey from their current locations
    def move0(self, xory):
        if random.random() < self.probabilityMove:
            if random.random() < 0.5:
                #print("increase y")
                xory = (xory + 1) % 300
            else:
                #print("decrease y")
                xory = (xory - 1) % 300
        return xory
        
    def move(self):
        self.print1("Before move:" + self.__str__())
        self.y = self.move0(self.y)
#        #print("moving")
#        if random.random() < 0.5:
#            if random.random() < 0.5:
#                #print("increase y")
#                self.y = (self.y + 1) % 100
#            else:
#                #print("decrease y")
#                self.y = (self.y - 1) % 100
        self.x = self.move0(self.x)
#        if random.random() < 0.5:
#            if random.random() < 0.5:
#                #print("increase x")
#                self.x = (self.x + 1) % 100
#            else:
#                #print("decrease x")
#                self.x = (self.x - 1) % 100
        self.print1("After move:" + self.__str__())
        
    def eat(self): # can you make it eat what is left?
        amount = random.randint(0,10)
        #amount = 2
        self.print1("Amount eaten " + str(amount))
        if self.environment[self.y][self.x] > amount:
            self.environment[self.y][self.x] -= amount
            self.store += amount
            
    def share(self,neighbourhood,agents,j): # can you make it eat what is left?
        # Go through agents
        for i in range(j + 1, len(agents)):
            d = self.distance(agents[i])
            self.print1("I am Agent " + str(self.name) + " do I share with Agent" + str(i) + "?")
            self.print1("The distance between us is " + str(d))
            if (d < neighbourhood):
                self.print1("Yes, we share.")
                self.print1("I have store " + str(self.store))
                self.print1("You have store " + str(agents[i].store))
                amount = (self.store + agents[i].store) / 2
                self.store = amount
                agents[i].store = amount
                self.print1("We end up sharing " + str(amount))
            else:
                self.print1("No, we are too far away to share.")

    def distance(self, agent):
        return (((self.y - agent.y)**2) + 
                ((self.x - agent.x)**2))**0.5
                
    def print1(self, s):
        if (self.printlevel > 1):
            print(s)
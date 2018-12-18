# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:31:00 2018

@author: ml17kfma
"""
import random # random is a library contains many featurs and now it is imported

# a classification of an agent characteristic and behavior that can move and eat and share with other agents within the environment given 
class Agent():

# initialise and define the variables that will be used in the model     
    def __init__(self, name, environment, randomSeed, probabilityMove, printlevel):
        random.seed(randomSeed) # this implimented to generlise the resulte of the model each time it will be run 
        self.x = random.randint(0, 299) 
        # The x coordinate value it can be obtained from a web page but here it is random number from 0 to 299 to be inside the environment boundaries   
        self.y = random.randint(0, 299)
        # The y coordinate value it can be obtained from a web page but here it is random number from 0 to 299 to be inside the environment boundaries
        self.name = name # the id of each agent
        self.environment = environment # The space that evrey agent will move in and eat from.
        self.store = 0 # The value of each agent store which could be a basket and it is zero here.
        self.probabilityMove = probabilityMove 
        # this variable will be used in defining the ability of agents to move into different place within the environment 
        self.printlevel = printlevel # this implemented to orgenise printing the values and textual contents
        pass
    
# This function will give every agent a specific name, location and store after running the model and it return all these values into the agents 
    def __str__(self):
        return "Agent " + str(self.name) + ": Location x=" + str(self.x) + "; y=" + str(self.y) + " Store=" + str(self.store)
 
# describe the movement ability of agents whether they move or stay from their current locations to different direction 
    def move0(self, xory):
        if random.random() < self.probabilityMove:
            if random.random() < 0.5:
                xory = (xory + 1) % 300
            else:
                xory = (xory - 1) % 300
        return xory
# define agent locations befor and after any new move for each iteration        
    def move(self):
        self.print1("Before move:" + self.__str__())
        self.y = self.move0(self.y)
        self.x = self.move0(self.x)
        self.print1("After move:" + self.__str__())
        
# describe the amount of eating of agents from the environment and decrease that from values of pixles          
    def eat(self): 
        amount = random.randint(0,10) # the amount of an agent eating will change randomly in each iteration
        #amount = 2
        self.print1("Amount eaten " + str(amount)) # show the value of amount eaten
        if self.environment[self.y][self.x] > amount: # condition if the amount below the value of environment they can eat
            self.environment[self.y][self.x] -= amount # take the value from environment
            self.store += amount # add the value to the store 
# share the with other agents using the condition inside the loop if distance between agents is below the neighbourhood             
    def share(self,neighbourhood,agents,j): 
        # Go through agents
        for i in range(j + 1, len(agents)): 
            d = self.distance(agents[i]) # set d variable as a distance of an agent
            self.print1("I am Agent " + str(self.name) + " do I share with Agent" + str(i) + "?")
            #a textual message cantains agents id with a quastion that asked if they share or not
            self.print1("The distance between us is " + str(d)) # the distance will appear 
            if (d < neighbourhood):
                self.print1("Yes, we share.") # if the above condition is true the agents will share otherwise they will not share 
                self.print1("I have store " + str(self.store)) # show the value of an agent store 
                self.print1("You have store " + str(agents[i].store)) # idicate the other agent store  
                amount = (self.store + agents[i].store) / 2 # every agent share half of their store 
                self.store = amount 
                agents[i].store = amount
                self.print1("We end up sharing " + str(amount)) # sum the amount of sharing 
            else:
                self.print1("No, we are too far away to share.")
# calculate the distance between agents according to their locations using x and y coordinate values
    def distance(self, agent):
        return (((self.y - agent.y)**2) + 
                ((self.x - agent.x)**2))**0.5
                
# define the print function which is described previously                
    def print1(self, s):
        if (self.printlevel > 1):
            print(s)
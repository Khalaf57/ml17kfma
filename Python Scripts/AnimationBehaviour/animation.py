# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:30:02 2018

@author: ml17kfma
"""
import random
import operator
import matplotlib.pyplot
import agentframework
import matplotlib.animation 
matplotlib.use('TkAgg')


#a = agentframework.Agent()
#print(a)
#print(a.x)
#print(a.y)
#a.move()
#print(a.x)
#print(a.y)
#
#b = agentframework.Agent()
#print(b)
#print(b.x)
#print(b.y)
#b.move()
#print(b.x)
#print(b.y)


                
#def distance_between(agents_row_a, agents_row_b):
##    return (((agents_row_a[0] - agents_row_b[0])**2) + 
##         ((agents_row_a[1] - agents_row_b[1])**2))**0.5
#    return (((agents_row_a.y - agents_row_b.y)**2) + 
#         ((agents_row_a.x - agents_row_b.x)**2))**0.5

num_of_agents = 10#3#10#2#10
num_of_iterations = 100#3
agents = []
neighbourhood = 25
probabilityMove = 0.4
variety = 40#9#10
printlevel1 = 1
printlevel2 = 2


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#def print1(s):
#    if (printlevel2 > 1):
#        print(s)

# load environment

print("Step 1: Load environment")
data = open("M:\Python Scripts\in2.txt")
#data = open("M:\Python Scripts\in.txt")
environment = []
for line in data: 
    parsed_line = str.split(line,",")
    rowlist = [] 
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)

data.close()
    
#environment.append(float(rowlist))
#print (environment)

 
# Make the agents.
print("Step 2: Create agents")
for i in range(num_of_agents):
     agents.append(agentframework.Agent(i, environment, i * variety, probabilityMove, printlevel2))

## Check to see that the agents can be plotted
#for i in range(num_of_agents):
#     #matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
#     matplotlib.pyplot.scatter(agents[i].x,agents[i].y,color="black")




# Move and eat.
     
def update(frame_number):
    
    fig.clear()
    
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    
    print("Step 3: Move, eat and share")
    #agentframework.print1("Move, eat")
    
    for i in range(num_of_agents):
        #agentframework.print1("Agent " + str(i))
        agents[i].move()
        agents[i].eat()
        #agentframework.print1("Share")
        #agents[i].share(neighbourhood,agents,i)
        
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        #print(agents[i].x,agents[i].y)
    
    matplotlib.pyplot.show()

## Move and eat and share.
#for j in range(num_of_iterations):
#     for i in range(num_of_agents):
#         agents[i].move()
#         agents[i].eat()
#         agents[i].share(neighbourhood,agents)
      
#         if random.random() < 0.5:
#             agents[i][0] = (agents[i][0] + 1) % 100
#         else:
#             agents[i][0] = (agents[i][0] - 1) % 100
#
#         if random.random() < 0.5:
#             agents[i][1] = (agents[i][1] + 1) % 100
#         else:
#             agents[i][1] = (agents[i][1] - 1) % 100

 
    


#matplotlib.pyplot.show()

"""
for i in range(num_of_agents):
    print(i)
    #matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y,color="red")
    """


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)

#for agents_row_a in agents:
#    for agents_row_b in agents:
#        distance = distance_between(agents_row_a, agents_row_b) 

#environment.append(rowlist)
#rowlist.append(value)
#rowlist = [] 
#environment = []



# Make the agents.
print("Step 4: Resulting agents")
for i in range(num_of_agents):
     print(agents[i])
     


#print (parsed_line)



#import fileinput
#a = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
#b = fileinput.input(a)
#for line in b:
#    print(b.filename())
#    print(line)
#b.close()


"""
f = open("M:\Python Scripts\in.txt")
data = []
for line in f:
    parsed_line = str.split(line,",")
    data_line = []
    for word in parsed_line:
        data_line.append(float(word))
#        print(float(word))
    data.append(data_line)
"""

"""
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + 
         ((agents_row_a[1] - agents_row_b[1])**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []


# Make the agents.
for i in range(num_of_agents):
     agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
     for i in range(num_of_agents):

         if random.random() < 0.5:
             agents[i][0] = (agents[i][0] + 1) % 100
         else:
             agents[i][0] = (agents[i][0] - 1) % 100

         if random.random() < 0.5:
             agents[i][1] = (agents[i][1] + 1) % 100
         else:
             agents[i][1] = (agents[i][1] - 1) % 100

 
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
     matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 
"""

"""
import random
import operator
import matplotlib.pyplot
import agentframework

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
   agents.append(agentframework.Agent())

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        agents[i].move()
 
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 
"""
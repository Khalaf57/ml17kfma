# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:30:02 2018

@author: ml17kfma
"""

"""
in this mode we creat agents that have a location which is craeted randomly between 0 and 299, these agents are moving randomly and eating 
the given environment from a file called ( in2.txt). Also agents share thier store with other agents within a neighbourhood if it in a certain distance

"""
#import libraries, time and the agentframework file
import random
import operator
import matplotlib.pyplot
import agentframework
import matplotlib.animation 
import tkinter
matplotlib.use('TkAgg')
import time


# start time at this stage of the model
start = time.clock ()               

# determain the number of agents in the model:
num_of_agents = 10#3#10#2#10
#num_of_iterations = 100#3 # this replaced by the update function
agents = []
# determin the distance of sharing the food between agents
neighbourhood = 40
# this describe the chance of moving each agents which is here 40%
probabilityMove = 0.4
# this give all agents a specific location each time the model run  
variety = 40
# create printing method to print values frequently:
printlevel1 = 1
printlevel2 = 2

# create a window as a user interface to run the model which have 2d screen to
# show the model and it has 7 units of width and 7 units of length  
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# load environment from a particular text file which called (in2). Firstly,a text message will be displyed 
# as a first step and then the file will be opened. After that there will be a loop to obtain values of environment into the environment 
# variable and each line of values will be separated. 
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
    

# Make the agents, previously we clarify the number of agents and in this stage we will create agents using i variable and each characteristic of an agent
# will be utilised from agentframework file such as the location of each agent and then it will be gained into i variable using the loop. 
#Also at the beginning of this stage a text message will be displayed  
print("Step 2: Create agents")
for i in range(num_of_agents):
     agents.append(agentframework.Agent(i, environment, i * variety, probabilityMove, printlevel2))

#create a variable that will be used in a couple of stages under the update function and the gen function  
carry_on = True

# Move and eat and share
# define the update function which will illustrate agents locations, movements, eating and sharing with neighbours within environment on the screen    
def update(frame_number):
    
    global carry_on
    fig.clear()
# display the envirnoment on the screen using x and y coordinates values which are between 0 and 299      
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
# show a textual content     
    print("Step 3: Move, eat and share")
    #agentframework.print1("Move, eat")
# using for which is a loop to demonstrate agents movements and eating and sharing     
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share(neighbourhood,agents,i)
        
    matplotlib.pyplot.imshow(environment)
#  display agents initial locations and uptade agents loctaions taking the agents new coordinates x and y values after the moving and show it on the screen. 
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

# this codition is implemented to stop the model operation when the random nember will be below 0.01 or it will continue until reach another codition under gen function.     
    if random.random() < 0.01:
        carry_on = False
        end = time.clock() # if the there is a stop condition set the time 
        print("stopping condition","time = " + str(end - start)) # display a textual content if the condition is true and show the running duration 

# define the gen function which is utilised instead of iterations to carry on the model process while the condition is false or the 
        # iterations is below 200.
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 200) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

# define run function which is implemented to show the animation of agents eating and sharing and moving on a user interface
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()
   
    
# create the user interface which has a title and drop down menu with a single command      
root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop() # wait until the user click on the command (run )


# set the time at the end of runing this model 
end = time.clock()
print ("time = " + str(end - start))


# displey the agents after the stop of the model
print("Step 4: Resulting agents")
for i in range(num_of_agents):
     print(agents[i])
     

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:30:02 2018

@author: ml17kfma
"""
import random
import operator
import matplotlib.pyplot
import agentframework_scrapwebpage
import matplotlib.animation 
import tkinter
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg
import requests
import bs4



num_of_agents = 10#3#10#2#10
#num_of_iterations = 100#3
agents = []
neighbourhood = 40
probabilityMove = 0.4
variety = 120#9#10
printlevel1 = 1
printlevel2 = 2


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])




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

#load x and y values of agents from a web page:    
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
# Make the agents.
print("Step 2: Create agents")
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework_scrapwebpage.Agent(i, environment, i * variety, probabilityMove, printlevel2, x , y))


        
carry_on = True

# Move and eat.
     
def update(frame_number):
    
    global carry_on
    fig.clear()
    
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
    
    print("Step 3: Move, eat and share")
    #agentframework.print1("Move, eat")
    
    for i in range(num_of_agents):
        #agentframework.print1("Agent " + str(i))
        agents[i].move()
        agents[i].eat()
        #agentframework.print1("Share")
        agents[i].share(neighbourhood,agents,i)
        
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x(),agents[i].y())
        #print(agents[i].x,agents[i].y)
    
    #matplotlib.pyplot.show()
    
    if random.random() < 0.01:
        carry_on = False
        print("stopping condition")


 
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 300) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1




def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()
   
    
    
root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop()



# Make the agents.
print("Step 4: Resulting agents")
for i in range(num_of_agents):
     print(agents[i])
     





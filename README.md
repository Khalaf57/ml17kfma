## Hellow World
My name is **Khalaf** and I am currently studying a Geographical Informations Systems (GIS) at the University of Leeds.
I am interested in Human Geography more than other aspects of geography. 


This page was created as a part of programming module requarimint in the GIS Master Course at The University of Leeds.

The "Hellow World" Model was developed through the course and I have attached all the practices which are 39 files. 
This model contains two Python files mode.py and agentframwork.py  

Moreover, the model creats agents which could be people or animales in the space and it describe their behaviors
such as an agent ability to move from place to another and agent  intractions with each other and with the environment
which has been represented by values of numbers. 

The agent communications are various due to random options and each agent should share the food collected within a certain distance which is here 50 units and represented by neighborhood. 
The initial location of agents in the environment  are made randomly and it can be obtained from a web page.
However, I could not utilise the coordinates of agents and implement x and y values in my model.


The final model can be seen in a folder called "Final_Model"

You can press on [ml17kfma](https://github.com/Khalaf57/ml17kfma/tree/master/Python%20Scripts) to go and preview the content of my
web page or you can click on the above  "View on GitHub" to access it .




### Examples of codes 


```markdown
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
    
```


## contact email

ml17kfma@leeds.ac.uk

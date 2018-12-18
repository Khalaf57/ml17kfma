## Hellow World
my name is **Khalaf** and I am currently studying a Geographical Informations Systems (GIS) at the University of Leeds 


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



1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Khalaf57/ml17kfma/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.

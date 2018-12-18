
import random
import operator
import matplotlib.pyplot
import time

start = time.clock ()
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

random_seed = 4324
random.seed(random_seed)

num_of_agents = 20
num_of_iterations = 1
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



'''
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)
'''
distance = distance_between(agents[0], agents[1])
print(distance)

# Calculate distance between all agents and maximum
maxdistance = 0
for i in range(num_of_agents):
    for j in range(num_of_agents):
        if (i > j):
            distance = distance_between(agents[i], agents[j])
            #print(i, j, "distance", distance)
            if (distance > maxdistance):
                maxdistance = distance
                #print("maxdistance", maxdistance)
print("maxdistance", maxdistance)

end = time.clock()
print ("time = " + str(end - start))
            
   
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()# write a comment of what the benifet of learning this method at the end of this lesson like ( we learnt about agents function )
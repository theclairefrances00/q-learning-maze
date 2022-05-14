import random
import math
from matplotlib import pyplot as plt
import numpy as np

# --------------- Create and display maze ---------------
n = 12
obst = 30

START = 0
FINISH = n*n

maze = [[1 for x in range(n)] for y in range(n)] 

for i in range(obst-1):
    maze[random.randint(1,n-1)][random.randint(1,n-1)] = -100

maze[0][0] = 1 # Start Point
maze[n-1][n-1] = 10 # End Point

plt.imshow(maze)
plt.text(-0.5, 0, "Start", fontsize=12, multialignment = 'center')
plt.text(n-1.5, n-1, "End", fontsize=12, multialignment = 'center')
            
plt.axis('off')
plt.show()


# --------------- Create Rewards Table ---------------
reward = [[1 for x in range(FINISH)] for y in range(FINISH)]
for i in range(FINISH):
    for j in range(FINISH):
        if j!=i-n and j!= i+n and j!=i-1 and j!=i+1:
            reward[i][j]= -math.inf


# --------------- Q-Learning ---------------
alpha = 0.1 #learning rate
q_table = np.random.normal(0, 1, (FINISH, FINISH)) # randomly initialized
gamma = 0.99 # discount factor
max_iter = 1000
for i in range(max_iter):
    curr_state = START
    while(True): # Until goal reached
        

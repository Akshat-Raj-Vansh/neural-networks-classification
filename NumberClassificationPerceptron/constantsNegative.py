#-1 : 111 1-11 1-11 1-11 111
#1 : -11-1 -11-1 -11-1 -11-1 -11-1
#2 : 111 -1-11 111 1-1-1 111
#3 : 111 -1-11 111 -1-11 111
#4 : 1-11 1-11 111 -1-11 -1-11
#5 : 111 1-1-1 111 -1-11 111
#6 : 111 1-1-1 111 1-11 111
#7 : 111 -1-11 -1-11 -1-11 -1-11
#8 : 111 1-11 111 1-11 111
#9 : 111 1-11 111 -1-11 111

import numpy as np

input_vector = np.array([[1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1],
                         [-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1],
                         [1,1,1,-1,-1,1,1,1,1,1,-1,-1,1,1,1],
                         [1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1],
                         [1,-1,1,1,-1,1,1,1,1,-1,-1,1,-1,-1,1],
                         [1,1,1,1,-1,-1,1,1,1,-1,-1,1,1,1,1],
                         [1,1,1,1,-1,-1,1,1,1,1,-1,1,1,1,1],
                         [1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1],
                         [1,1,1,1,-1,1,1,1,1,1,-1,1,1,1,1],
                         [1,1,1,1,-1,1,1,1,1,-1,-1,1,1,1,1]])

# 1-1 X 15
m,x = input_vector.shape

target_vector = np.array([[-1,-1,-1,-1],
                          [-1,-1,-1,1],
                          [-1,-1,1,-1],
                          [-1,-1,1,1],
                          [-1,1,-1,-1],
                          [-1,1,-1,1],
                          [-1,1,1,-1],
                          [-1,1,1,1],
                          [1,-1,-1,-1],
                          [1,-1,-1,1]])

# 1-1 X 4
n,t = target_vector.shape

input_nodes = 15

output_nodes = 4
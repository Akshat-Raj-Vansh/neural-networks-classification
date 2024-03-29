#0 : 111 101 101 101 111
#1 : 010 010 010 010 010
#2 : 111 001 111 100 111
#3 : 111 001 111 001 111
#4 : 101 101 111 001 001
#5 : 111 100 111 001 111
#6 : 111 100 111 101 111
#7 : 111 001 001 001 001
#8 : 111 101 111 101 111
#9 : 111 101 111 001 111

import numpy as np

input_vector = np.array([[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1],
                         [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0],
                         [1,1,1,0,0,1,1,1,1,1,0,0,1,1,1],
                         [1,1,1,0,0,1,1,1,1,0,0,1,1,1,1],
                         [1,0,1,1,0,1,1,1,1,0,0,1,0,0,1],
                         [1,1,1,1,0,0,1,1,1,0,0,1,1,1,1],
                         [1,1,1,1,0,0,1,1,1,1,0,1,1,1,1],
                         [1,1,1,0,0,1,0,0,1,0,0,1,0,0,1],
                         [1,1,1,1,0,1,1,1,1,1,0,1,1,1,1],
                         [1,1,1,1,0,1,1,1,1,0,0,1,1,1,1]])

# 10 X 15
m,x = input_vector.shape

target_vector = np.array([[0,0,0,0],
                          [0,0,0,1],
                          [0,0,1,0],
                          [0,0,1,1],
                          [0,1,0,0],
                          [0,1,0,1],
                          [0,1,1,0],
                          [0,1,1,1],
                          [1,0,0,0],
                          [1,0,0,1]])

# 10 X 4
n,t = target_vector.shape

p = 4
from numpy import array, sign
from numpy.lib.function_base import append
from constants import *

alpha = 0.05
b = np.zeros(t)
v = np.random.randn(x,p) * 0.01
w = np.random.randn(p,t) * 0.01

delK = 0 # error correction weight for output layer
delJ = 0 # error correction weight for hidden layer

def binary_sigmoid(z):
    return 1/(1+np.exp(-z))

def derivative_binary_sigmoid(z):
    _z = binary_sigmoid(z)
    return (_z * (1-_z))

def train():

    iterations = 0
    while(iterations < 1000):
        iterations += 1
       
        # calculating inputs for hidden layer
        
        # input_vector = 10X15
        # v = 15X4
        # z = 10X4
        zin = b + np.dot(input_vector, v)
        z = binary_sigmoid(zin)

        # calulating inputs for output layer
        yin = b + np.dot(z,w)
        y = binary_sigmoid(yin)

        # delK = 10X4
        # w = 4X4
        # z = 10X4
        delK = (target_vector - y) * derivative_binary_sigmoid(yin) 
        for i in range(n):
            for j in range(t):
                for k in range(p):
                    w[k][j] = w[k][j] + alpha * delK[i][j] * z[i][j]
        
        del_in_j = np.dot(delK, w);
        delJ = del_in_j * derivative_binary_sigmoid(zin)
        for i in range(m):
            for j in range(p):
                for k in range(x):
                    v[k][j] = v[k][j] + alpha * delJ[i][j] * input_vector[i][k]
        
        # error = np.sqrt(0.5 * np.sum((target_vector-y)**2))
        error = 0
        for i in range(m):
            error += 0.5 * np.sum((target_vector[i] - y[i]) ** 2)
        print("Error: {}".format(np.sqrt(error)))

if(__name__ == "__main__"):
    train()
    print("Training Complete")
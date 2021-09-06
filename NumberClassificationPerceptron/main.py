from numpy import array, sign
from numpy.lib.function_base import append
from constantsNegative import *

alpha = 0.03
b = np.zeros(t)
w = np.random.randn(x,t)

def train():
    flag = 1

    while(flag != 0):
        # calculating net input and then response at each node
        yin = b + np.dot(input_vector, w)
        y = sign(yin)
        # print(yin)
        # print(y)

        flag = 0
        errors = 0
        #adjusting the weights
        for i in range(n):
            for j in range(t):
                # if expected and actual output are different
                if(target_vector[i][j] != y[i][j]):
                    errors += 1
                    flag = 1
                    # adjust the weight and bias accordingly
                    for a in range(x):
                        deltaW = alpha * target_vector[i][j] * input_vector[i][a]
                        # print("deltaW:{}".format(deltaW))
                        w[a][j] = w[a][j] + alpha * target_vector[i][j] * input_vector[i][a]
        print(errors)
                

            

        # print(target_vector[2])
        # print(y[2])
        # print((target_vector[2] != y[2]).astype(int))

def predict(user_input):
    yin = b + np.dot(user_input, w)
    y = sign(yin)
    print(y)


if(__name__ == "__main__"):
    train()
    print("Training Complete. Enter your input:")
    user_input = array([])
    for i in range(15):
        v = int(input())
        user_input = append(user_input, v)
    print(user_input)
    predict(user_input)
# Neural Networks for Classification
The given models have been created for an assignment. 

## Alphabet classification using Perceptron
Using the basic perceptron algorithm, inputs and outputs have been mapped and output is being predicted properly. The program can be run using
`python main.py`. 
Furthermore, you can give a custom input and it will predict the proper alphabet. Input is in the form of a 5X3 matrix. For example to represent A, you need to type in 
```
1  1 1
1 -1 1
1  1 1
1 -1 1
1 -1 1
```

The output that is predicted is a list of binary bits (5 bits) to represent an alphabet in its decimal form. For A, it will print as
```
-1 -1 -1 -1 1
```
which evaluates to 1 that is the 1st letter of alphabet

## Number classification using Perceptron
Using the basic perceptron algorithm, inputs and outputs have been mapped and output is being predicted properly. The program can be run using
`python main.py`. 
Furthermore, you can give a custom input and it will predict the proper digit (0-9). Input is in the form of a 5X3 matrix. For example to represent 5, you need to type in 
```
 1  1  1
 1 -1 -1
 1  1  1
-1 -1  1
 1  1  1
```

The output that is predicted is a list of binary bits (4 bits) to represent a digit in its decimal form. For 5, it will print as
```
-1 1 -1 1
```

## Number classification using Back Propagation 
Through back propagation, the model minimizes the error between the target_vector and output (y). Currently it reduces to 2% error only and there are 1000 iterations.
The numbers can be modified as per user.

Similar to Number classification through Percptron, the inputs and outputs have been mapped from 5X3 matrix to a 4 bit binary number. However, the -1 have been swapped with 0 for better readability. 
Activation function used is binary sigmoidal function for this model

## Contribution
If you find any errors in the model, kindly send a PR. They are not the perfect models, but they do the job :)

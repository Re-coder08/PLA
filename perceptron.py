#dependencies
import numpy as np
import random
from training import create_data, plot_anything
from matplotlib import pyplot as plt

lr = 0.2
# Creating weights
weights = np.zeros(3)
# print("weights : " + str(weights))

# Initializing weights values
def init_weight(weights):
    for i in range(len(weights)):
        weights[i] = random.randint(-1,1)
        # print("weight : " + str(weights[i]))

init_weight(weights)

# Activation Function
def sign(value):
    if value >= 0:
        return 1
    else:
        return -1

# summation and guessing function
def guess(inputs, weights):
    sum = 0
    for i in range(len(weights)):
        sum += inputs[i] * weights[i]

    output = sign(sum)
    return output

# print("data : " + str(create_data(10)))


inputs = np.asarray(create_data(50))
targets = inputs[:,[3]]
# print("targets : " + str(targets))
# print("input : " + str(inputs))
only_inputs = inputs[:,[0,1,2]]
# print("new_inputs = " +str(only_inputs))

#training weights
def train(weights, targets, only_inputs, inputs):

    # inputs = np.asarray(create_data(10))
    # targets = inputs[:,[3]]
    # # print("targets : " + str(targets))
    # # print("input : " + str(inputs))
    # only_inputs = inputs[:,[0,1,2]]
    # # print("new_inputs = " +str(only_inputs))

    for l in range(len(only_inputs)):
        # print("inputs = " + str(only_inputs))
        guess_ans = guess(only_inputs[l], weights)
        # print("guess : " + str(guess_ans))
        error = targets[l] - guess_ans
        for i in range(len(weights)):
            weights[i] += error * only_inputs[l][i] * lr

        print("weights updating : " + str(weights) + " | input : " + str(only_inputs[l]) + " | error : "+ str(error) + " | target : " + str(targets[l]) + " | guess : " + str(guess_ans) )

train(weights, targets, only_inputs, inputs)

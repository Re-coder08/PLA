import numpy as np
import random
from matplotlib import pyplot as plt

class perceptron:

    lr = 0.05
    input = []
    def __init__(self, weights):
        self.weights = weights

    def init_weight(self):
        w = []
        for i in range(self.weights):
            w.append(random.randint(0,5))
        return w

    def guess(self, w, data):
        # print("input : " + str(self.input))
        sum = 0
        for i in range(len(w)):
            sum += data[i] * w[i]
            # print("sum = " + str(sum))

        output = self.sign(sum)
        return output

    def sign(self, value):
        if value >= 0:
            return 1
        else:
            return -1

    def create_data(self, value):
        data = []
        target = []
        for i in range(value):
            self.x = random.randint(0, 20)
            self.y = random.randint(0, 20)
            self.bias = 1
            if self.x > self.y :
                self.label = 1
            else:
                self.label = -1

            self.input = [self.x, self.y, self.bias]
            data.append(self.input)
            target.append(self.label)
        # print("input = " + str(data))

        return data, target


    def train(self, passes, data, target, weights):
        # print("data = " + str(data))
        # print("inittial_weight = " +str(weights))
        # print(target)
        for _ in range(passes):
            # print("========================= pass no: " + str(_))
            for i in range(len(data)):
                # print("single_data = " + str(data[i]))
                error = 0
                # print(i)
                # print("weight = " +str(weights))
                guessed = self.guess(weights, data[i])
                # print("guessed : " + str(guessed))
                # print(target[i])
                error = target[i] - guessed
                # print("error = " +str(error))
                for j in range(len(weights)):
                     weights[j] += error * data[i][j] * self.lr
                # print("updated weight : " + str(weights))
        return weights

    def testing(self, data, targets, w):
        for i in range(len(data)):
            print(data[i])
            final_result = w[-1] * 1 + w[0] * data[i][0] + w[1] * data[i][1]

            final_error = targets[i] - self.sign(final_result)
            print("final_error = " +str(final_error))

def ploting(data, targets, weights):
    print("data : " + str(data))
    print("targets : " + str(targets))
    pos = []
    neg = []
    for i in range(len(targets)):
        if targets[i] == 1:
            pos.append(data[i][0:2])
        else:
            neg.append(data[i][0:2])
    print("pos = " + str(pos))
    print("neg = " + str(neg))
    pos = np.asarray(pos)
    neg = np.asarray(neg)
    posx = pos[:,[0]]
    posy = pos[:,[1]]
    negx = neg[:,[0]]
    negy = neg[:,[1]]
    print("pox = " + str(posx) )
    plt.scatter(posx,posy,color ="red")
    plt.scatter(negx,negy,color = "blue")
    plt.plot([0,20],[0,20], marker = 'o')
    plt.show()


p = perceptron(3)
weights = p.init_weight()
data = p.create_data(10)
test_data = data[0][5:]
test_targets = data[1][5:]
# data1 = [[12, 19, 1], [4, 10, 1], [6, 8, 1], [15, 1, 1], [10, 19, 1], [12, 14, 1], [6, 3, 1], [9, 5, 1], [1, 1, 1], [9, 18, 1]]
# ploting(data[0], data[1], weights)
# print("data = " +str(data[0]))
# print("target = " + str(data[1]))
# for i in range(10,1):
result = p.train(50, data[0][0:5], data[1][0:5], weights)
print("final weights : " +str(result))
final = p.testing(test_data, test_targets, result)
print(final)

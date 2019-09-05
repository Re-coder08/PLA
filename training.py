#dependencies
import random
import numpy as np
from matplotlib import pyplot as plt

data_points = 10

def point():
    x = random.randint(0, 20)
    y = random.randint(0, 20)
    bias = 1
    if x > y :
        label = 1
    else:
        label = -1

    return bias, x, y, label

# print("single data : " + str(point()) )


def create_data(data_points):
    data = []
    for _ in range(data_points):
        data.append(np.asarray(point()))

    # print(data)
    return data
# create_data(data_points)

def ploting(data):
    xspot = []
    yspot = []
    label = []
    for i in data:
        xspot.append(i[0])
        yspot.append(i[1])
        label.append(i[2])

    # print("xspot = " + str(xspot))

    plt.scatter(xspot, yspot)
    plt.show()
    # plt.plot(plot_data)
    # plt.show()

# ploting(create_data(data_points))

def plot_anything(data):
    pos = []
    neg = []
    pos_x = []
    pos_y = []
    neg_x = []
    neg_y = []

    for i in data:
        if i[-1] == 1:
            pos.append(i[0:2])
        else:
            neg.append(i[0:2])
    # print("pos : " + str(pos))
    # print("neg : " + str(neg))

    for j in pos:
        pos_x.append(j[0])
        pos_y.append(j[1])
    # print("pos_x : " + str(pos_x))
    # print("pos_y : " + str(pos_y))

    for k in neg:
        neg_x.append(k[0])
        neg_y.append(k[1])
    # print("neg_x : " + str(neg_x))
    # print("neg_y : " + str(neg_y))


    plt.scatter(pos_x, pos_y, color='red')
    plt.scatter(neg_x, neg_y, color='blue')
    linex = [0, 0]
    liney = [20, 20]
    # plt.plot([20,0],[20,0], marker = 'o')
    plt.plot([0,20],[0,20], marker = 'o')
    plt.grid()
    plt.show()

# plot_anything(create_data(data_points))

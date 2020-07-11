from random import uniform
from globalVariablesAndFunctions import *


def sign(num):
    # The sign function just tells you if the given number is positive or negative
    # In this case the sign function an activation function

    if num >= 0:
        return 1

    else:
        return -1


class Perceptron():
    weights = []

    def __init__(self, number_of_input_nodes=3):

        # number of Nodes in the first layer [default: (x1, x2, bias)]
        self.number_of_input_nodes = number_of_input_nodes

        # initializing weights of Neural Network (Perceptron) with random numbers between -1 and 1
        for i in range(self.number_of_input_nodes):
            self.weights.append(uniform(-1, 1))

    def predict(self, inputs):
        # The predict method calculates the weighted sum of inputs (inputs * their weight)
        # and returns the the sign of the weighted sum
        # we can train our Perceptron based on its predictions
        # and as we train our Perceptron more and more, its predictions get closer to the target

        weighted_sum = 0
        for i in range(self.number_of_input_nodes):
            weighted_sum += inputs[i] * self.weights[i]
        output = sign(weighted_sum)
        return output

    def train(self, inputs, target):
        # The train method is the most important part of the Perceptron
        # It calculates error of each weight and adjusts each weight by based on the amount of its error times learning rate (and obviously times input)
        # learning rate is a hyper_parameter so it can be what ever you want BUT you have to find the learning rate that works better ( for you )

        prediction = self.predict(inputs)
        error = target - prediction
        learning_rate = 0.001
        for i in range(self.number_of_input_nodes):
            self.weights[i] += error * inputs[i] * learning_rate

    def predicted_line(self, x):
        # returns the slope-intercept of the line (based on predicted m and b) mapped to the height of the window

        m = -(self.weights[0] / self.weights[1])
        b = -(self.weights[2] / self.weights[1])
        y = m * x + b
        return int(mapx(y, -1, 1, height, 0))

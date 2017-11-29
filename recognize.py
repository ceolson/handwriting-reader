from random import *
import math
import numpy as np
from keras.models import Sequential

def sigmoid(x):
    return exp(x) / (exp(x) + 1)

# Takes in a string containing the pixels as an array
def recognize(image, coefficients, biases, sizes):
    layers = Layers()
    layers.first = [pixel for pixel in image]

    sizes.first = len(layers.first)

    for layer_number in range(1, 4):
        layer = layer_list[layer_number]
        for i in range(sizes[layer]):
            total = 0
            for j in range(sizes.layer_list[layer_number - 1]):
                total = total + layers.layer_list[layer_number - 1][j] * coefficients.layer[i][j] + biases.layer[i]
            layers.layer.append(sigmoid(total))

    return layers.output

def cost(image, coefficients, biases, sizes, target):
    output = recognize(image, coefficients, biases, sizes)
    cost = 0
    for i in range(10):
        if i = target:
            cost += abs(1 - output[i])
        else:
            cost += abs(output[i])
    return cost

# Initialize random coefficients and biases

sizes = [None, 20, 20, 10]
coefficients = []
biases = []

for layer_number in range(1,4):
    layer = layer_list[layer_number]
    for i in range(sizes.layer):
        coefficients[i].append([])
        for j in range(sizes.layer_list[layer_number - 1]):
            coefficients[i][j].append(randint(-1, 1))
        biases[i].append(randint(-1, 1))

recognize(image, sizes, coefficients, biases)


model = Sequential()


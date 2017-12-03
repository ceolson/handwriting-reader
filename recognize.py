import keras
import numpy as np
from keras.models import load_model
from MNIST import get_test_data
import random

def recognize(image):
    nn = load_model("modely.h5")

    image2 = [[]]
    for row in image:
        for pixel in row:
            image2[0].append(pixel)

    image_array = np.array(image2)
    print(image_array)
    predictions = nn.predict(image_array)[0]

    maximum = 0
    max_place = None
    for i in range(len(predictions)):
        if predictions[i] > maximum:
            maximum = predictions[i]
            max_place = i
    return max_place
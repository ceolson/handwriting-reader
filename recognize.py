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

    predictions = nn.predict(image_array, batch_size=12)

    print(type(predictions), type(predictions[0]), predictions)
    rounded = [round(x[0]) for x in predictions]
    return rounded

    # max = 0
    # for i in range(len(prediction_array)):
    #     if prediction_array[i] > max:
    #         max = prediction_array[i]
    #         return i
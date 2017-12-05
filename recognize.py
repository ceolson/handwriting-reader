import keras
import numpy as np
from keras.models import load_model
from MNIST import get_test_data
import random

def recognize(image):
    nn = load_model("modely.h5")

    image_2dim = [[]]
    for row in image:
        for pixel in row:
            image_2dim[0].append(pixel)

<<<<<<< HEAD
    image_array = np.array(image2)

    #print(image_array)
=======
    image_array = np.array(image_2dim)
>>>>>>> 8278f57ed0ec3a11e75f651b08b7cfa5b39a4889

    predictions = nn.predict(image_array)[0]

    maximum = 0
    max_place = None
    for i in range(len(predictions)):
        if predictions[i] > maximum:
            maximum = predictions[i]
            max_place = i
    return max_place

def re_learn(image, label):
    model = load_model("modely.h5")

    model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

    image_2dim = [[]]
    for row in image:
        for pixel in row:
            image_2dim[0].append(pixel)

    image_array = np.array(image_2dim)
    label_array = [[]]
    label_array[0].append(label)

    labels = np.array(label_array)
    data = image_array

    # Convert labels to categorical one-hot encoding
    one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)

    # Train the model, iterating on the data in batches of 32 samples
    model.fit(data, one_hot_labels, epochs=10, batch_size=32)

    model.save("/Users/ceolson/cs/cs50/handwriting-reader/modely.h5")

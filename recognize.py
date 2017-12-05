import keras
import numpy as np
from keras.models import load_model
from MNIST import get_test_data
import random

def recognize(image):
    # Get model from storage on server
    model = load_model("modely.h5")

    # Enclose image in another set of brackets and remove array structure
    image_2dim = [[]]
    for row in image:
        for pixel in row:
            image_2dim[0].append(pixel)

    image_array = np.array(image_2dim)

    # Predict!
    predictions = model.predict(image_array)[0]

    # Read prediction array and return what the character should be
    maximum = 0
    max_place = None
    for i in range(len(predictions)):
        if predictions[i] > maximum:
            maximum = predictions[i]
            max_place = i

    return max_place

def re_learn(image, label):

    # Get model from storage on server
    model = load_model("modely.h5")

    # Compile for learning
    # Copied from ttps://keras.io/getting-started/sequential-model-guide/
    model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

    # Add another set of brackets
    image_2dim = [[]]
    for row in image:
        for pixel in row:
            image_2dim[0].append(pixel)


    data = np.array(image_2dim)

    # Format labels correctly
    label_array = [[]]
    label_array[0].append(label)
    labels = np.array(label_array)

    # Convert labels to categorical one-hot encoding
    # Copied from ttps://keras.io/getting-started/sequential-model-guide/
    one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)

    # Train the model
    model.fit(data, one_hot_labels, epochs=10)

    # Save the model
    model.save("/Users/ceolson/cs/cs50/handwriting-reader/modely.h5")

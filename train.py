from random import *
import math
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from MNIST import get_training_data, get_test_data
import h5py

# Make new model, add some layers
# Lots of syntax taken from hhttps://keras.io/getting-started/sequential-model-guide/
# Some lines directly copied

model = Sequential()

model.add(Dense(units=50, activation='relu', input_dim=28 * 28))
model.add(Dense(units=20, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

# Directly from https://keras.io/getting-started/sequential-model-guide/
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

data_pairs = get_training_data()

labels = data_pairs[0]
data = data_pairs[1]

# Directly from https://keras.io/getting-started/sequential-model-guide/

# Convert labels to categorical one-hot encoding
one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)

# Train the model, iterating on the data in batches of 32 samples
model.fit(data, one_hot_labels, epochs=10, batch_size=32)

# Save model
model.save("/Users/ceolson/cs/cs50/handwriting-reader/modely.h5")

# # ________________________________________________________________

# # This part prints an evaluation, not necessary to run

# test_pairs = get_test_data()

# x_test = test_pairs[1]
# y_test = test_pairs[0]

# one_hot_labels2 = keras.utils.to_categorical(y_test, num_classes=10)

# score = model.evaluate(x_test, one_hot_labels2, batch_size=128)

# print(score)





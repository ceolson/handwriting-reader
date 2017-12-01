import numpy as np

# Simple script to extract MNIST data and return array of tuples
def get_training_data():
    file1 = open('data/train-labels-idx1-ubyte', 'r', encoding = "ISO-8859-1")
    labels = file1.read()

    file2 = open('data/train-images-idx3-ubyte', 'r', encoding = "ISO-8859-1")
    images = file2.read()

    label_array = []
    image_array = []

    for i in range(60000):
        temp_image = []
        for j in range(28 * 28):
            value = images[16 + 28 * 28 * i + j]
            pixel_value = int(value.encode("hex"), 16)
            temp_image.append(pixel_value)
        label =  labels[8 + i]
        image_array.append(temp_image)
        label_array.append(int(label.encode("hex")))

    return (np.array(label_array),np.array(image_array))

def get_test_data():
    file1 = open('data/t10k-labels-idx1-ubyte', 'r', encoding = "ISO-8859-1")
    labels = file1.read()

    file2 = open('data/t10k-images-idx3-ubyte', 'r', encoding = "ISO-8859-1")
    images = file2.read()

    label_array = []
    image_array = []

    for i in range(10000):
        temp_image = []
        for j in range(28 * 28):
            value = images[16 + 28 * 28 * i + j]
            pixel_value = int(value.encode("hex"), 16)
            temp_image.append(pixel_value)
        label =  labels[8 + i]
        image_array.append(temp_image)
        label_array.append(int(label.encode("hex")))

    return (np.array(label_array),np.array(image_array))

a = get_training_data()
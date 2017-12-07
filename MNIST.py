import numpy as np
import binascii as b

# Helper function to convert things like "\x0a" to things like "11"
def dehexify(string):
    return(int(ord(string)))

# Simple program to extract MNIST data and return array of tuples
def get_training_data():   
    file1 = open('data/train-labels-idx1-ubyte', 'r', encoding = "ISO-8859-1")
    labels = file1.read()

    file2 = open('data/train-images-idx3-ubyte', 'r', encoding = "ISO-8859-1")
    images = file2.read()

    label_array = []
    image_array = []

    # Loop over all images and turn them into lists
    for i in range(60000 - 1):
        temp_image = []

        # The size of a singe image
        for j in range(28 * 28):

            # Read image string, after offset of 16 and some multiple of image size
            value = images[16 + 28 * 28 * i + j]

            # Convert from weird MNIST hexadecimal formatting
            pixel_value = dehexify(value) / 255

            temp_image.append(pixel_value)

        # Read labels after offset of 8
        label = labels[8 + i]

        # Add both to array of images and labels
        image_array.append(temp_image)
        label_array.append(dehexify(label))

    return (np.array(label_array),np.array(image_array))

# Same as above, but for the test data
def get_test_data():
    file1 = open('data/t10k-labels-idx1-ubyte.gz', 'r', encoding = "ISO-8859-1")
    labels = file1.read()

    file2 = open('data/t10k-images-idx3-ubyte.gz', 'r', encoding = "ISO-8859-1")
    images = file2.read()

    label_array = []
    image_array = []

    for i in range(10000 - 1):
        temp_image = []
        for j in range(28 * 28):
            value = images[16 + 28 * 28 * i + j]
            pixel_value = dehexify(value) / 255
            temp_image.append(pixel_value)
        label =  labels[8 + i]
        image_array.append(temp_image)
        label_array.append(dehexify(label))

    return (np.array(label_array),np.array(image_array))

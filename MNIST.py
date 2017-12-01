import numpy as np
import binascii as b

def dehexify(string):
    # string_fix = ""
    # for char in string:
    #     if char != "/" and char != "x":
    #         string_fix += char
    # return int(string_fix, 16)
    return(int(ord(string)))


# Simple script to extract MNIST data and return array of tuples
def get_training_data():
    try:    
        file1 = open('data/train-labels-idx1-ubyte', 'r', encoding = "ISO-8859-1")
        labels = file1.read()

        file2 = open('data/train-images-idx3-ubyte', 'r', encoding = "ISO-8859-1")
        images = file2.read()

        label_array = []
        image_array = []

        for i in range(60000 - 1):
            temp_image = []
            for j in range(28 * 28):
                value = images[16 + 28 * 28 * i + j]
                pixel_value = dehexify(value)
                temp_image.append(pixel_value)
            label =  labels[8 + i]
            image_array.append(temp_image)
            label_array.append(dehexify(label))

        return (np.array(label_array),np.array(image_array))
    except IndexError:
        print(i)

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
            pixel_value = dehexify(value)
            temp_image.append(pixel_value)
        label =  labels[8 + i]
        image_array.append(temp_image)
        label_array.append(dehexify(label))

    return (np.array(label_array),np.array(image_array))

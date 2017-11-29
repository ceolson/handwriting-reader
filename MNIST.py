def get_training_data():
    file1 = open('train-labels-idx1-ubyte', 'r')
    labels = file1.read()

    file2 = open('train-images-idx3-ubyte', 'r')
    images = file2.read()

    data = []

    for i in range(60000):
        temp_image = []
        for j in range(28 * 28):
            temp_image.append(images[16 + 28 * 28 * i + j]) 
        data.append((temp_image,labels[8 + i]))

    return data

data = get_training_data()
print(data[14])
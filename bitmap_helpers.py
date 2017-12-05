import math
import numpy as np

# Chops off equal rows or columns from each side of an image array to make it square
def squareify(matrix):
    new_matrix = []
    diff = len(matrix) - len(matrix[0])

    # Nothing to change
    if diff == 0:
        new_matrix = matrix

    # Need to chop off rows
    elif diff > 0:
        top = round(diff / 2)
        bot = len(matrix) - (diff - top)
        new_matrix = matrix[top:bot]

    # Need to chop off columns
    elif diff < 0:
        front = round(abs(diff) / 2)
        back = len(matrix[0]) - (diff - front)
        for row in matrix:
            new_row = row[front:back]
            new_matrix.append(new_row)

    return np.array(new_matrix)

# Scales a square matrix to 
# Adapted from CS50 staff solution to problem set 4
# Assumes square matrix for the scale to work properly
def scale_to(matrix, size):

    # Calculates scaling factor
    f = size / len(matrix)

    # Horizontal stretch
    h_scaled = []

    for row in matrix:
        new_row = []
        for i in range(size):
            # Finds the corresponding place to take pixel from
            index = math.floor(i / f)
            new_row.append(row[index])
        h_scaled.append(new_row)

    # Vertical stretch
    v_scaled = []

    for i in range(size):
         # Find corresponding row
        index = math.floor(i / f)
        v_scaled.append(h_scaled[index])

    return np.array(v_scaled)

# Turns image to grayscale and to 0.0-1.0 pixels instead of RGB intensities
# Adapted from http://www.tannerhelland.com/3643/grayscale-image-algorithm-vb6/
def gray(matrix):
    new_matrix = []

    for row in matrix:
        new_row = []
        for pixel in row:

            # This just takes the red intensity
            # Called "average" because this can also be an average of RGB intensities
            average_intensity = pixel[0]

            # Scales 255-0 to 0.0-1.0
            bw = (255 - average_intensity) / 255

            # If pixel is close to white, turns it to pure white
            if bw < 0.5:
                bw = 0.0

            new_row.append(bw)
        new_matrix.append(new_row)
            
    return np.array(new_matrix)

# This just packs a bunch of functions here into one thing to call
def process(matrix):
    square = squareify(matrix)
    scaled_matrix = scale_to(square, 28)
    gray_matrix = gray(scaled_matrix)
    return gray_matrix

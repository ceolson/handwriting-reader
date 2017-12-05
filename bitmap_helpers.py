import math
import numpy as np

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


def scale_to(matrix, size):
# Adapted from CS50 staff solution
# ASSUMES SQUARE MATRIX!!

    f = size / len(matrix)

    # Horizontal stretch
    h_scaled = []

    for row in matrix:
        new_row = []
        for i in range(size):
            index = math.floor(i / f)
            new_row.append(row[index])
        h_scaled.append(new_row)

    # Vertical stretch
    v_scaled = []

    for i in range(size):
        index = math.floor(i / f)
        v_scaled.append(h_scaled[index])

    return np.array(v_scaled)

def gray(matrix):
# Adapted from http://www.tannerhelland.com/3643/grayscale-image-algorithm-vb6/

    new_matrix = []

    for row in matrix:
        new_row = []
        for pixel in row:
            average_intensity = pixel[0]
            bw = (255 - average_intensity) / 255
            if bw < 0.5:
                bw = 0.0
            new_row.append(bw)
        new_matrix.append(new_row)
            
    return np.array(new_matrix)

def process(matrix):
    square = squareify(matrix)
    scaled_matrix = scale_to(square, 28)
    gray_matrix = gray(scaled_matrix)
    return gray_matrix



# Given a square matrix in 2D array. Write a program to flip the matrix in-place, transpose the matrix in-place, and rotate the matrix(anti-clockwise) in-place.

'''
flip_matrix function will flip the matrix horizontally provided in-place
'''

def flip_matrix(matrix):
    print("Matrix before flipping", matrix)
    matrix_size = len(matrix)
    for row in range(matrix_size):
        matrix[row] = matrix[row][::-1]
    print("Matrix after flipping", matrix)

'''
transpose_matrix function will do transpose of the matrix provided in-place
'''

def transpose_matrix(matrix):
    print("Matrix before transpose", matrix)
    matrix = list(zip(*matrix))
    print("Matrix after transpose", matrix)

'''
roatate_matrix function will roatate the matrix in anti-clockwise direction by 90 deg in-place
'''

def rotate_matrix(matrix):
    print("Matrix before rotation", matrix)
    matrix_size = len(matrix)
    for row in range(matrix_size):
        matrix[row] = matrix[row][::-1]
    for row in range(matrix_size):
        for col in range(row, matrix_size):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    print("Matrix after rotation", matrix)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flip_matrix(matrix)
transpose_matrix(matrix)
rotate_matrix(matrix)
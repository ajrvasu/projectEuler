""" In the 20×20 grid below, four numbers along a diagonal line have been marked in red. The product of these numbers is 26 × 63 × 78 × 14 = 1788696. What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid? """

# Converting number.txt file into a matrix of numbers 

import numpy as np  

filename = "euler11.txt"

with open(filename,"r") as lines:
    array =[]
    for line in lines:
        array.append(line)

newArray =[]
for i in array:
    j = i.split(' ')
    k = [int(n) for n in j]
    newArray.append(k)
print(newArray)

matrix = np.asmatrix(newArray)
shape = np.shape(matrix)
rows, columns =  shape[0], shape[1]

def largestProduct(n, matrix):
    max = 0
    for i in range (0, rows):
        for j in range (0, columns-n):
            product = matrix[i,j] * matrix[i,j+1] * matrix[i,j+2] * matrix [i,j+3]
            if product >= max:
                max = product
    for i in range (0, rows-n):
        for j in range (0, columns):
            product = matrix[i+1,j] * matrix[i+2,j] * matrix[i+3,j] * matrix [i+4,j]
            if product >= max:
                max = product
    for i in range (0, rows-n):
        for j in range (0, columns-n):
            product = matrix[i,j] * matrix[i+1,j+1] * matrix[i+2,j+2] * matrix [i+3,j+3]
            if product >= max:
                max = product
    for i in range (0,rows-n):
        for j in range (columns-1,n+1,-1):
            product = matrix[i,j] * matrix[i+1,j-1] * matrix[i+2,j-2] * matrix [i+3,j-3]
            if product >= max:
                max = product
    return max
       
print(largestProduct(4, matrix))
            
import numpy as np

# Broadcasting allows NumPy to perform operations on arrays with different shapes 
# by virtually expanding dimensions so that match the larger array's shape.

# Two arrays are compatible for broadcasting if:-
# For each dimension(layer, column, row) 

# The dimensions have the same size. 
# OR
# One of the dimensions has a size of 1.

array1 = np.array([[1, 2, 3, 4]])  #2d array with only one row and 4 column (1x4)

array2 = np.array([[1],            #2d array with 4 rows and 1 column (4x1)      
                   [2], 
                   [3], 
                   [4]])

print(array1.shape) #(1, 4) 
print(array2.shape) #(4, 1) 

#row ka dimension of array1 will be compared to row ka dimension of array2
#column ka dimension of array1 will be compared to column ka dimension of array2
#We read dimensions from right to left, the dimension don't match but one of them is 1. See for each. They are compatible.

print(array1*array2)  #we got a 2d array with 4x4

array3 = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12], 
                   [13, 14, 15, 16]])
array4 = np.array([[1], 
                   [2],
                   [3],
                   [4]])
print(array3.shape)
print(array4.shape)

print(array3*array4)


#Multiplication table via broadcasting

first = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) #1x10 matrix
second = np.array([[1],                             
                   [2],                             #10x1 matrix
                   [3],
                   [4],
                   [5],
                   [6],
                   [7],
                   [8],
                   [9],
                   [10]])

print(first.shape)
print(second.shape)
print(first*second)







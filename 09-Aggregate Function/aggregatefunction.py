# Aggregate functions = summarizes data and typicall returns a single value

import numpy as np

array1 = np.array([[2, 3, 4, 5, 18],
                  [7, 8, 9, 10, 1]])

# np.sum() function
# It is used to find sum of all the elements present in the matrix

print(np.sum(array1))


# np.mean() function
# It gives the average of all the elements present in the matrix

print(np.mean(array1))


# np.std() function
# It gives standard deviation, which is measure of spread in your data, statistic term

print(np.std(array1))


# np.var() function
# It is variance, another statistic term, it is the square of a standard deviation

print(np.var(array1))


# np.min() function
# It gives minimum value from the elements in the array

print(np.min(array1))


# np.max() function
# It gives maximum value from the elements in the array

print(np.max(array1))


# np.argmin() function
# To get position of the minimum value, it just start counting from start from 0 

print(np.argmin(array1)) 


# np.argmax() function
# To get the position of the maximum value

print(np.argmax(array1))

array1 = np.array([[2, 3, 4, 5, 18],
                  [7, 8, 9, 10, 1]])

# To select and access specific things

# For eg we want to sum all columns
#When axis = 0 , we are applying this function(sum) to all the columns
print(np.sum(array1, axis=0)) #it gives a matrix with 1 row x no. of columns, wahi ek row me sare columns 
#Vertical Closing of function being applied

#When axis = 1, we are applying this function(sum) to all the rows
print(np.sum(array1, axis=1)) #no. of rows x 1 column
#Linear/Horizontal closing





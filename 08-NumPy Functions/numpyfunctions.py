import numpy as np

#np.zeros() = returns an array of zeros, but you have to pass in the shape of the array
#you pass in layers, rows, and columns as a tuple, i.e., one more () and then integers

#array = np.zeros(10) #returns a 1d array with all 0, 10 elements
#array = np.zeros((5, 4)) #returns a 2d array with 5 rows and 4 columns, all element 0
#array = np.zeros((2, 3, 10)) #returns a 3d array with 2 layers, 3 rows and 10 columns, all element 0

#---------------------------------------------------------------------------------------------------------
#np.ones() = returns an array of ones, but you have to pass in the shape of the array
#you pass in layers, rows, and columns as a tuple, i.e., one more () and then integers
#array = np.ones(3) #1d array with all elements 1, 3 elements
#array = np.ones((3,5)) #2d array with all elements 1, 3 rows and 5 columns
#array = np.ones((3, 4, 2)) #3d array with all elements 1, 3 layers, 4 rows and 2 columns


#---------------------------------------------------------------------------------------------------------
#np.full() = returns an array with specific value, but you have to pass in the shape of the array, 
#          and that specific value as another parameter

#array = np.full((3, 4), 6) #makes a 2d array with 3 rows and 4 columns with elements 6 in each
#array = np.full((2, 3, 4), 69) #makes a 3d array with 2 layers, 3 rows and 4 columns, with elements 69 in each


#---------------------------------------------------------------------------------------------------------
#np.eye() = it will create an identity matrix, you only need to pass number of rows, it will make a square matrix
# Identity matrix is useful for linear algebra and matrix math

#array = np.eye(5) #creates an indentity matrix of 5x5


#---------------------------------------------------------------------------------------------------------
#np.empty() = creates an empty array, you have to pass in the shape of the array
# you pass in layers, rows, and columns as a tuple, i.e., one more () and then integers
# it add garbage value from your memory as elements
# np.empty() is faster than np.zeros()
#array = np.empty((3, 3, 4))


#---------------------------------------------------------------------------------------------------------
#np.arange() = it has three arguments (start, stop, step), gives 1d array with the values you put it in range
#ofcourse start is inclusive and stop is exclusive
#We are not in control of number of elements

#array = np.arange(0, 100, 0.2) # created a 1d array with elements 0 to 100, and step 2 so 0, 2, 4 and so on
#step could be in decimal too


#---------------------------------------------------------------------------------------------------------
#np.linspace() = means linear space, (start, stop, num)
# stop is inclusive here 
# It creates an array with evenly spaced values, similar to .arange() but different is
# We will define the number of points that we want

#array = np.linspace(2, 100, 4)   #4 elements, evenly spaced between 2 and 100
array = np.linspace(0, 50, 9) 
print(array)
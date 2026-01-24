import numpy as np


#We need consistent number of elements
#Zero dimensional array, think of it like a single point
array = np.array('A')
print(array)
print(array.ndim)  #to access the dimension of the array, .ndim stands for number of dimensions
print('---------------')

#1 dimensional array, like a single row
array_1 = np.array(['A', 'B', 'C']) #Elements are now contained in a list
print(array_1)
print(array_1.ndim)
print('---------------')

#2 dimensional array, like rows and columns, 3x3 matrix or 2d array
array_2 = np.array([[1, 2, 5],          #we added one more list outside then, we added more pair of 1d list separated by ,
                    [3, 4, 9], 
                    [5, 6, 11]])  
print(array_2)
print(array_2.ndim)
print('---------------')

#3 dimensional array, enclose 2d list with another list
array_3 = np.array([[['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I']], #layer 0
                    [['J', 'K', 'L'],['M', 'N', 'O'],['P', 'Q', 'R']], #layer 1
                    [['S', 'T', 'U'],['V', 'W', 'X'],['Y', 'Z', '^']]]) #layer 2
#we added one more list outside then, we added more pairs of 2d list separated by ,
print(array_3)
print(array_3.ndim)
print(array_3.shape) #you can also access shape using .shape attribute, for 3d it gives 
                     #(depth or layers, no. of rows, no. of columns)

array_3 = np.array([[['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I']], #layer 0
                    [['J', 'K', 'L'],['M', 'N', 'O'],['P', 'Q', 'R']], #layer 1
                    [['S', 'T', 'U'],['V', 'W', 'X'],['Y', 'Z', '^']]]) #layer 2 
print(array_3[0][1][2]) #this is called Chain indexing, we do this in python

#But in NumPy we can use Multidimensional indexing

print(array_3[2, 1, 0])  #Multidimensional Indexing, it is faster than chain indexing


#Making word with string concatenation
word = array_3[0, 1, 0] + array_3[0, 2, 1] + array_3[1, 2, 2] + array_3[2, 0, 2] + array_3[2, 1, 0]
print(word)

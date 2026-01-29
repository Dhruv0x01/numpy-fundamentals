import numpy as np


#We need consistent number of elements
#Zero dimensional array, think of it like a single point
array = np.array('A')
print(array)
print(array.ndim)  #to access the dimension of the array, .ndim stands for number of dimensions
print('---------------')

#1 dimensional array, like a single row, 1 list basically
array_1 = np.array(['A', 'B', 'C']) #Elements are now contained in a list
print(array_1)
print(array_1.ndim)
print('---------------')

#2 dimensional array, like rows and columns, 3x3 matrix or 2d array
#(rows, columns)
array_2 = np.array([[1, 2, 5],          #we added multiple 1d array, separated them by comma(,)  
                    [3, 4, 9],          #and then contained the whole thing with another [ ]
                    [5, 6, 11]])  
print(array_2)
print(array_2.ndim)
print('---------------')

#3 dimensional array, enclose 2d list with another list
#We made multiple 2d lists and then separate them by comma(,) and then contained the whole thing with []
#(layers, rows, columns)

#To access a certain element from a 3d array
#variablename[layer of the element, row of that element, columns of that element]

array_3 = np.array([[['A', 'B', 'C'],       #layer 0
                     ['D', 'E', 'F'],
                     ['G', 'H', 'I']],
                       
                    [['J', 'K', 'L'],       #layer 1
                     ['M', 'N', 'O'],
                     ['P', 'Q', 'R']],
                       
                    [['S', 'T', 'U'],       #layer 2
                     ['V', 'W', 'X'],
                     ['Y', 'Z', '^']]
                    ]) 
print(array_3)
print(array_3.ndim)
print(array_3.shape) #you can also access shape using .shape attribute, for 3d it gives 
                     #(depth or layers, no. of rows, no. of columns)
print(array_3[0,1,2])


array_3 = np.array([[['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I']], #layer 0
                    [['J', 'K', 'L'],['M', 'N', 'O'],['P', 'Q', 'R']], #layer 1
                    [['S', 'T', 'U'],['V', 'W', 'X'],['Y', 'Z', '^']]]) #layer 2 
print(array_3[0][1][2]) #this is called Chain indexing, we do this in python

#But in NumPy we can use Multidimensional indexing

print(array_3[2, 1, 0])  #Multidimensional Indexing, it is faster than chain indexing


#Making word with string concatenation
word = array_3[0, 1, 0] + array_3[0, 2, 1] + array_3[1, 2, 2] + array_3[2, 0, 2] + array_3[2, 1, 0]
print(word)

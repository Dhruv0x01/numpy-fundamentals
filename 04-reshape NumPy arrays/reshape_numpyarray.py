import numpy as np

# reshape() = Changes the shape of an array w/o altering its underlying data
#             .reshape(rows, columns)
# the reshape() function return an array which we will reassign

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
array = array.reshape(3, 4)  #make sure the total number of elements remain same even in the new shape array


print(array)
print(array.shape)

#Reshaping in 3 dimensional array
# .reshape(layers, rows, columns)

array_2 = np.array(['A', 'B', 'C' , 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
                    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'])
array_2 = array_2.reshape(3, 4, 2) #3 layers, 4 rows, and 2 columns
print(array_2)
print(array_2.shape)

#Another way 
array_3 = np.array(['A', 'B', 'C' , 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
                    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'])
array_3 = array_3.reshape(3, -1, 4)  #on adding -1 as layers, numPy will decide the layer based on rows and columns, but it should be possible too
print(array_3) #there can be only one unknown dimension
print(array_3.shape)

# In ML libraries like scikit-learn, we will often see the .reshape() function used with -1

import numpy as np

my_list = [1, 2, 3, 4]
my_list *= 2               #This ends up duplicating all existing elements

print(my_list)

#Creating NumPy array

array = np.array([1, 2, 3, 4])
array *= 2               #Here all the elements in the array get multiplied by 2
print(array)
print(type(array))

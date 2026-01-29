import numpy as np

# Scalar arithmetic (Means single value)

array = np.array([1.01, 2.5, 3.99])

print(array + 1) #Each element will have 1 added to it
print(array - 2) #Subtract 2 from each element
print(array * 3) #Multiple 3 to each element
print(array / 4) #Divided each element by 4
print(array ** 5) #Raise each element to the power of 5, power of operator = **

#Vectorized math functions (Means 1d list)
#We can apply a function to an entire array without writing a loop
#NumPy library does have some inbuilt math function

#print(np.sqrt(array))
#print(np.round(array)) #to round
#print(np.floor(array)) #round down/ GIF
#print(np.ceil(array)) #round up/ LIF

print(np.pi) #builtin constants

#1. Find area of circle corresponding to each radii
radii = np.array([1, 2, 3])

area = np.pi * radii ** 2
#area = np.round(area)

print(area)

#Element-wise arithmetic

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array2 / array1)
print(array1 ** array2)

#Comparison operators

scores = np.array([91, 55, 100, 73, 82, 64])

print(scores == 100)  #We are seeing if any of the element of the scores is equal to 100
print(scores >= 60)
print(scores < 60)

#Filtering
#variablename[condition] = whatever you want those satisfying condition to be turned into
scores[scores<60] = 0 #basically any element which is under 60 will be considered 0/fail
print(scores)



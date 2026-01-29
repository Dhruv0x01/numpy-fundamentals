# dtype = Keyword argument that tells NumPy what kind of values are stored in an array
#         Otherwise NumPy guesses the best type based on your data
#         Manually setting dtype improves performance
#         & is more memory efficient (especially when working with large data sets)

# integer (int8, int16, int32, int64) number after int represents the number of bits allocated to store that number
# float (float16, float32, float64)
# boolean (bool_) 1 byte per element
# string (str_, <U#) 
# object (object_) be cautious with objects

import numpy as np

print("integer")
int_array = np.array([1, 2, 3, 4, 5])
print(int_array )
print(int_array .dtype) #currently we are using 64bits to hold each element of the array 
print(f"{int_array .nbytes} bytes") # the array use 40 bytes, 8 bits = 1 byte , 64 bits = 8 bytes , 8bytes*5elements = 40 bytes

#Manually changing dtype
print("After changing dtype")
int_array= np.array([1, 2, 3, 4, 5], dtype = np.int8) #It doesn't matter much rn as we have only 5 elements
print(int_array)                          #But it's really good in case of very high number of elements say 1 million
print(int_array.dtype) #int8
print(f"{int_array.nbytes} bytes")  #8 bits = 1 byte, hence 5 elements with 1 byte, = 5 bytes

#int8 can only hold number from -128 to 127
#int16"""""""""""""""""""" from -32,768 to 32,767
#int32"""""""""""""""""""" from -2,147,483,648 to 2,147,483,647
#int64"""""""""""""""""""" from -9.22e18 to 9.22e18 

print("---------------------------")
print("Floating point number")
float_array = np.array([1.2, 2.3, 4.2, -8.9, 10.21])
print(float_array)
print(float_array.dtype) #float64, hence 64 bits is used to store each element
print(f"{float_array.nbytes} bytes") #8 bits = 1 byte, 64 bits = 8 bytes, 5 elements * 8 bytes each = 40 bytes

print("After changing dtype")
float_array = np.array([1.2, 2.3, 4.2, -8.9, 10.21], dtype = np.float16)
print(float_array)
print(float_array.dtype) #float16
print(f"{float_array.nbytes} bytes") #8 bits = 1 byte, 16 bits = 2 byes each, 10 bytes total

print("---------------------------")
print("Boolean")
bool_array = np.array([0, 12, 2, 3.25, -4, 5], dtype = np.bool_)  #.bool_ is for numpy boolean, .bool is the python boolean
print(bool_array)   #anything non-zero will be considered true 
print(bool_array.dtype) #bool
print(f"{bool_array.nbytes} bytes") #1 byte each, 6 bytes total

print("---------------------------")
print("Strings")
string_array = np.array([10, 111, 24114, 3414656, 4, 514156666], dtype=np.str_)
print(string_array) #numbers are converted to strings
print(string_array.dtype) #<U1, U is for unicode, number next to U represents number of maximum characters out of all elements
print(f"{string_array.nbytes} bytes")
print("---------------------------")
print("Next example")
string2_array = np.array(["apple", "mango", "banana", "guava", "watermelon"], dtype = np.str_)
print(string2_array)
print(string2_array.dtype)
print(f"{string2_array.nbytes} bytes")
print("---------------------------")
print("Setting dtype to explicitely to a fixed length unicode string, so no element is more than that fixed string length")
string2_array = np.array(["apple", "mango", "banana", "guava", "watermelon"], dtype = "<U4") #limited number of characters to 4
print(string2_array)
print(string2_array.dtype)
print(f"{string2_array.nbytes} bytes")
print("---------------------------")

obj_array = np.array([1, 2.2, True , "4", 5], dtype = np.object_)
print(obj_array)
#Be cautious when working with objects, operations fall back to python not NumPy optimized C code
#We lose the speed advantages when working with python objects
#But this does allows you to mix and match data types
#Creating NumPy array of objects could be necessary when working with:-
# custom classes, datetime objects, or when we are planning it to convert it to pandas later


print("------------------")
print("To convert one data type to another after already creating your array")
#We use .astype() function

array_eg = np.array([1.2, 2.6, 3.9, 4.2, 5.145]) #currently an integer array
array_eg = array_eg.astype(np.int16) # converted to int, basically the part after decimal got removed

print(array_eg)
print(array_eg.dtype)
print(f"{array_eg.nbytes} bytes")


                                                                

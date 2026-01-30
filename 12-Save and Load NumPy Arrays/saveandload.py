import numpy as np

# Save a single NumPy array
# Using np.save() function, 
# np.save("file name", the array name) This saves the array in our folder only
# np.save("absolute file location", array name) Here we specified the location for the file to be saved in

#array = np.array([[1, 2, 3],
                  #[4, 5, 6]])

#np.save("data", array)                             #This saves the array in our folder only, with the name being data
#np.save("C:\\Users\\Dhruv\\Desktop\\data", array)  #Here we gave absolute file location and the end \\data made the file name data
                                                    
#print("NumPy array was saved!") #Just for confirmation, not compulsory

#-----------------------------------------------------------------------------------------------------------

# To load a single NumPy array

# variable = np.load("file path") , the load function will return an array, we loaded that array into the variable we created

#arr = np.load("C:\\Users\\Dhruv\\Desktop\\data.npy") #here the .npy is imp

#print(arr) #Shape is maintained

#-----------------------------------------------------------------------------------------------------------

# Save multiple NumPy array
# np.savez() function, z means zipped
# np.savez("filename", list all array separated by , that you want to have it saved)
# all array will be saved in one file


#array1 = np.array([[1, 2, 3,],
#                  [4, 5, 6]])

#array2 = np.array([1.5, -4.2, 8.91, 1.11])

#array3 = np.array([[5, 9, 10, 19, 11], 
#                  [9, 10, 144, 192, 1],
#                  [90, 76, 45, 32, 13]])

#np.savez("multiplearray", array1, array2, array3) #We can add specified location too

#print("Your arrays are saved")


# If you are working with a lot of data, then you can store those arrays as compressed zip
# np.savez_compressed()
# It will take less memory,better when we are sharing it online but is slower to load and work with

#np.savez_compressed("compressed", array1, array2, array3)


#-----------------------------------------------------------------------------------------------------------

# Load multiple NumPy array

arrays = np.load("compressed.npz") #this file is the np.savez() one

array1 = arrays["arr_0"]
array2 = arrays["arr_1"]
array3 = arrays["arr_2"]

#print(arrays) #you can't directly print the zip, you have to use key for it
print(array1) 
print(array2)
print(array3)








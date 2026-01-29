import numpy as np

#array1 = np.array([[1, 2, 3, 4], 
#                  [5, 6, 7, 8], 
#                  [9, 10, 11, 12], 
#                  [13, 14, 15, 16]]) #2d array

# To slice array we use this
# variablename[start:end:step] this is called slice operator
#start is inclusive, end is exclusive like [1, 2) 


#Row Slicing -------------------------------------------------------------
# array[1] this will give only 2nd row
# array[-1] this will give you last row, -2 second last, and so on

#print(array1[0:3]) # [0, 3) include 1st row, 2nd row and 3rd row
#print(array1[1:3]) # [1, 3) include 2nd row and 3rd row

# array1[0] will give only 1st row
# array1[0:] will give from 1st row till end, we will need that :
#print(array1[0:]) #if you want to select up until the end

#print(array1[0::2]) #means select every 2nd row starting from 1st, 1st 3rd 5th and so on

#if we are selecting all rows, you can leave out the start and end as blank but the : : are req
#print(array1[::2])

#print(array1[::-1]) #if we entered the step as -1, this will return all the rows reversed

#Column Slicing-----------------------------------------------------

#array1 = np.array([[1, 2, 3, 4], 
#                   [5, 6, 7, 8], 
#                   [9, 10, 11, 12], 
#                  [13, 14, 15, 16]])
#first index is for the row, and second for the column

#print(array1[0, 0])  #first row, first column
#print(array1[:, 0])  #All rows, first column #Column 1
#print(array1[:, 1])  #Column 2
#print(array1[:, 2])  #Column 3
#print(array1[:, -1]) #last column


#Now selecting range

#print(array1[:, 1:]) #All rows and column from 2nd to last
#print(array1[:, 1::2]) #All rows and selecting every 2nd column
#print(array1[:, ::-1]) #All rows and reverse the order of columns
#print(array1[::-1,:])  #Reversed rows, and all columns
#print(array1[::-1, ::-1]) #Reversed rows and reversed columns



#Rows and Columns Slicing---------------------------------------------
array1 = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12], 
                   [13, 14, 15, 16]])

print(array1[:2, :2]) #only first two rows and columns
print(array1[:2, 2:]) #first two rows and 3rd and 4th column
print(array1[2:, :2]) #last two rows and 1st two columns
print(array1[1:3, 1:3]) #mid ke 4
print(array1[2:, 2:]) #last two rows and columns




import numpy as np
# jump = [[1,2,3],[4,5,6],[7,8,9]]
# dump = np.array(jump) # a way to create an array
# print(dump)
# print(np.arange(0,10)) # a way of creating arrays akin to using ranges
# print(np.zeros((3,2))) # used to generate an array of zeros np.zeros((rows,columns),dtype,)
# print(np.linspace(0,10,10)) # generates arrays by providing a start, stop and number of points, it generates a 1D array
# print(np.eye(3)) # generates an identity matrix
# print(np.random.rand(3,3)) # generates an array of specified dimension with a random distribution of numbers
# print()
# print(np.random.randn(3,3)) # generates an array of specified dimension with a normal distribution of numbers
# print()
# print(np.random.randint(1,10,10)) # generates a 1D array with a start, stop and number of elements

    ## Array Methods
# arr.reshape(a,b) - generates a new array containing the same elements as the previous one but with new elements
# arr.max() - shows the maximum element in an array
# arr.min() - shows the minimum element in an array
# arr.argmax() - shows the position of the max element
# arr.argmin() - shows the position of the min element
# arr.dtype() - shows the type of data in an array

        ## Indexing Numpy Arrays
# Numpy Arrays are indesed much like lists
# arr = np.arange(1,11)
# print(arr[6:])
# # numpy arrays can be broadcasted
# arr[0:5] = 10
# print(arr)
## a slice of an array isnt a copy of the original array but rather a view of the original array
## the array.copy() method should be used if a copy is to be created
# 2D arrays can be indexed in two ways
DArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print([DArray[0][1]]) ## indexing using double brackets
print(DArray[0,1])## indexing using singles brackets
# in order to index submatrices of a 2D array we use slice notation
print(DArray[1:,2:])
arr = np.arange(1,10)
bools = arr > 5
print(DArray[2:,1:])
print(bools)
print(arr[arr>5]) # indexing an array using a conditional statement
arre = np.arange(50).reshape(5,10)
print(arre[1:3,1:3])


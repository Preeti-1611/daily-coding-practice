'''import numpy as np 
arr = np.array([4,5,6,7,7,])
print(arr)

#2d
arr2d = np.array([[3,4,5],[6,7,8]])
print(arr2d)

#3d
arr3d =np.array([[[1,2,3],[4,5,6],[3,4,5]]])
print(arr3d)
print(arr3d.ndim) #dimension of array
print(arr3d.shape) #shape of array

'''
#checking nukmpy of numpy
'''import numpy as np
print(np.__version__)

arr = np.array([[2,3,4,5,6.5,67],[5,7,9,7,7,6]],float)# value of each array size should match with each other
print(arr)
print(type(arr)) #type of array
print(arr.dtype)#datatype of array
print(arr.ndim) #dimension of array
print(arr.size) #size of array
print(arr.shape) #shape of array
'''

#0d array
'''import numpy as np
arr = np.array(23)
print(arr)
print(arr.ndim)
print(arr.shape)#shape of array is o/p ==()
print(arr.dtype)

#3d array
a3 = np.array([
    [[2,3],[3,6]],
    [[4,8],[7,8]]
])

print(a3)
print(a3.ndim)
print(a3.shape) #2 blocks ,each block has 2 rows  each row has 2 columns
'''

#indexing
'''import numpy as np 
arr = np.array([2,4,5,7,3])
print(arr[4]+arr[4]) #indexing starts from 0
print(arr[-2]-arr[-4]) #negative indexing starts from -1

arr2 = np.array([[3,4,5],[6,7,8]])
print("indexing for 2d array")
print(arr2.ndim)
print(arr2[1][2]) #1nd row 2st column
print(arr2[0][1]) #0th row 1st column
print("hello for 3d array")
'''
'''import numpy as np
# third element of the second array of the first array
arr = np.array([[
    [1, 2, 3], [4, 5, 6]], 
    [[7, 8, 9], [10, 11, 12]]
    ])
print(arr[0, 1, 2])
print(arr.shape) # (2, 2, 3)
print(arr.ndim) # 3
'''




#dtype
import numpy as np 
arr = np.array([4,2,3],dtype ='S')
print(arr.dtype) #datatype of array
print(arr) # it will print in byte format b'4' b'2' b'3'
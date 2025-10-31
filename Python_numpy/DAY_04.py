from numpy import *
'''a1 =array([2,3,4,5,6,7])
print(sqrt(a1))
# print(sqet(a1))
print(sum(a1))
print(min(a1))
print(max(a1))
print(mean(a1))
print(median(a1))
print(sin(a1))
print(cos(a1))


print(log(a1))

#conactenation'
arr1 = array([1,2,3,4])
arr2 = array([5,6,7,8,9])
print(concatenate((arr1,arr2)))

'''
#same ouput
'''b1 =array([2,3,4,5,6])
b2 =b1
print(b1)   # [2 3 4 5 6]
             #[2 3 4 5 6]
print(b2)

print(id(b1))   #same id
print(id(b2))

'''
'''d1=array([3,4,5])
d2=d1.copy()
print(d1)
print(d2)
d1[2]=23
print(d1)
print(d2)
d2[1]=34
print(d2)
'''

#matrix

arr1 = array([
    [1,2,3],
    [4,5,6]
    
])
''''print(arr1)
print(arr1.ndim)  #2
print(arr1.dtype)  #int32
print(arr1.shape)  #(2, 3)
print(arr1.size)
'''''
# arr2 = arr1.flatten()
# print(arr2)
# print(arr2.ndim)


h1 = array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
])
print(h1.ndim)# 2
#convert 2d into 1d
h2 = h1.flatten() #1d
print(h2)
print(h2.ndim) #1d
#convert 1d into 2d
h3 = h2.reshape(2,6)    #2d 
print(h3)
print(h3.ndim)  #2d


#convert 1d into 3d
h4 = h2.reshape(2,3,2)  #3d     
print(h4)
print(h4.ndim)  #3d


import numpy as np

arr = np.array([[1, 2], [3, 4]])
flat_arr = arr.flatten()

print("Original Array:")
print(arr)

print("Flattened Array:")
print(flat_arr)

import numpy as np

arr = np.arange(12)   # creates array [0, 1, 2, ..., 11]
new_arr = arr.reshape(2, 3, 2)

print("Original Array:")
print(arr)

print("\nReshaped 3D Array:")
print(new_arr)



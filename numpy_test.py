import numpy as np

print(np.__version__)
arr = np.array([2,3,4,5])
print(arr)

arr1 = np.array((2,4,5,3,3))
print(arr1)
print(type(arr1))
print(type(arr))

#
# d0 = np.array(3)
# print(d0)
# d1 = np.array([4,6,2,1,3,2,4])
# print(d1)
# d2 = np.array([[7,4,2,1,4],[5,3,3.2,2,1]])
# print(d2)
# dd2= np.array([[4,6],[4.7,5]])
# print(dd2)

d3 = np.array([[[3,4,2],[5,8,6]],[[3,5,6],[4,8,2]]])
print(d3)
print(d3[0,1,2])
#dimensional check
print(d3.ndim)
print(d2.ndim)

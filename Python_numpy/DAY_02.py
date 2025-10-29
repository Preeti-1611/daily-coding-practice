# 2d array
'''
import numpy as np
arr =np.array([[3,4,5],[4,5,6]])
print(arr)
print()
'''

'''

from numpy import *
arr = array([34,34,22,12,33])
print(arr)
print(arr.dtype) #datype of array
print(arr.ndim) #dimension of array'''


#impliclity changing
'''from numpy import *
r1 = array([3,4,2,3,7.5]) #here i am changing the 7 to 7.5 it will convert entire array to float
print(r1)
print(r1.dtype)

r2 =array([3,6,2,6,4.4],int) #here i am explicitly changing the array to float
print(r2.dtype)
'''


#linspace
from numpy import *
d1 = linspace(0,15,34)
d2 = linspace(2,67)
print(d1)
print(d2)

#arange
a1 = arange(1,15,2)
print(a1)

#logspace
l1 = logspace(1,40,8)
print(l1)

#zeros
z1 =zeros(9)
print(z1)

#ones
o1 = ones(8,int) # int type also we can give
print(o1)
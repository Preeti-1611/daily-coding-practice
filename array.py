'''from array import *

vals = array('i',[32,322,3,23,2,3])
print(vals.buffer_info())
print(vals.typecode)

#output: (address, length)

print(vals.itemsize) #size of each item in bytes
vals.reverse()
print(vals)
print(vals[0])
'''
'''
import array as arr
n1 = arr.array('i',[4,5,2,4,-3,2])
for i in range(len(n1)):
    print(n1[i])
print("completed")

for e in n1:
    print(e)

i =0
while i<len(n1):
    print(n1[i])
    i+=1'''
import array as arr
a1 =arr.array('i',[])
n = int(input("enter the array number of elemnets:"))
for i in range(0,n):
    x = int(input(f"enter the value {i}:"))
    a1.append(x)
print(a1)

print(a1.index(4))

a1.remove(2)
print(a1)

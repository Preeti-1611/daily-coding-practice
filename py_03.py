x=4
x=str(x)
print(str(x))
print(type(x))
#case sensitive
Name="preeti"
name="adu"
print(name)
print("Name")
x,y,z =2,3,4
print(y)
x=y=z=34
print(z)
#methos in str
a="hello"
a.upper()
print(a.upper())
print(a.lower())
print(a.replace('h','G'))
name = "preeti"
adress="adress"
print(name is adress)
print(name is not adress)
#bitwise
x=3
y=6
print(x&y)
print(x|y)
print(x^y)
a=5
print(a>>3)
b=6
print(b<<4)
print(9>>3)
print(8<<3)
print(3>>2)
print(8<<2)
print(4<<5)
print(5>>3)

#list
list = ["apple","banana","cherry"]
print(list)
print(list[0])
print("apple" in list)
print("ghcv" not in list)
list[2]="vuv"
print(list)
list.insert(1,"ctxh")
print(list)
print(len(list))
list.append("fvvh")
print(len(list))
print(list.pop())
print(list)
list.append("hello")
print(list)
list.pop()
print(list)
new_list =[2,3,4,5,3,6]
new_list.reverse()
print(new_list)
new_list.sort()
print(new_list)
new1=[31,3,3,2]
new2 =[4,3,2,5]
new3 =new1.copy()
new1.append(56)
print(new3)
print(new1)



#tuple


'''
my_tuple = ("apple", 45, 342, "cherry")  # original tuple
tuple2 = list(my_tuple)                  # convert to list
tuple2.append("gsgr")                    # add element
my_tuple = tuple(tuple2)                 # convert back to tuple
print(my_tuple)

'''




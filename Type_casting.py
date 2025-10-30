x=10
y =2.5
z=x+y
print(z)
print(type(z))


a = "25"
b = int(a) #converting string to integer
c = float(b) #converting integer to float
print(a,type(a))
print(b,type(b))
print(c,type(c))
'''
#error cannnot convert string to integer
x="h"
print(type(x))
print(int(x))

c ="hii"
print(type(c))
y = int(c)
print(y,type(y))

'''

x = 10
y ="62"
print(int(y) + x)

p ="12.7"
q=float(p)
r = int(q)
print(q,r)

num = 45
text = str(num)
print("the number is " + text)
print(type(text))


a ="123"
b ="456" 
print(int(a)+int(b))


x = [1,2,3]
y = tuple(x)
z = set(x)
print(y)
print(z)

marks = [80, 90, 100]
text = str(marks)
print(text)
print(type(text))



a = True 
b = int(a)
c =float(a)
print(b,c)


num = 5.99
print(int(num))
print(str(num))


val = 0
print(bool(val))

val = "Hello"
print(bool(val))


x = [1, 2, 3]
y = str(x)
print(y)
print(type(y))

a = "3.14"
print(int(float(a)))


# Convert this list into a string:
# fruits = ["apple", "banana", "cherry"]
# Expected output: 'apple banana cherry'
fruits = ["apple", "banana", "cherry"]
result = " ".join(fruits)
print(result)



sentence = "Python is fun"
words = sentence.split()
print(words)

x = "10a"
print(int(x))



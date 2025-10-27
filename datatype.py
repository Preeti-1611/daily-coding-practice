'''#int float complex

x=45
print(type(x))
y=34.67
print(type(y))
v=-97637
print(v,type(v))
h=5j #complex
print(h,type(h))

'''
'''
# type conversion
x=45
y=34.56432
print(int(y))
print(float(x))
print(str(x))
print(complex(x))

'''
'''
# string
print('hello')
print("hello world")
a='car'
print(a)
x="preeti"
print(x)
#multiline str
a=""" hi this is me preeti nagarale from belgaum
"""
print(a)
'''
''' #strings in array
x="hello world"
print(x[3])
print(x[6])
print(x[2:8])
print(x[:2])
print(x[2:])

for i in "preetinagarale":
    print(i)

for x in "hi":
    print(x)

for j in "hello":
    print(j)'''

# sting length
a = "hello everyone"
print(len(a))
# looping through a string



'''#check string
txt = " the best moive"
print("best","m" in txt,txt)

sts="the one who never fails"
if "who" in sts:
    print('this is here')

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")'''

#slicing
b="hello world"
print(b[4:7])
print(b[3:6])
print(b[:7])
print(b[6:])
print(b[:])
print(b[-5:-1])

a="hello"
print(a.upper())
print(a.lower())

b="   nivcdvbv   "
print(b.strip())

x = "preeti"
print(x.replace("ee","vce"))

# split string
y="hemml"
print(y.split())

#concatination
a ="hello"
b="world"
print(a+b)
# formatted string
age= 56
print(f"my age is {age}")

a=34
b=6
print(a&b)
print(a|b)

print(a>>3)
print(b<<7)
print(a>>4)

c=20
d=30
print(id(a))
print(id(b))
print(a is b)

a ="hello"
b="world"
print(id(a))
print(id(b))
print(a is b)

a=30
b=20
a=a+b
print(a)
b=a-b
a=a-b
# print(a,b)

# swaping
a=10
b=20
a,b=b,a
a=b
b=a
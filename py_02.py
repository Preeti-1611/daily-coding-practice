'''matrix = [[1,2,3],
          [4,5,6],
          [4,6,7]]
print(matrix[0])
print(matrix[0][2])
print(matrix[1][1])

for row in matrix:
    for item in row:
        print(item)

#list methods
num =[3,5,7,2,2]
num.append(13)
print(num)
num.insert(3,45)
print(num)
num.remove(3)
print(num)
#clear method
print(num)
num.pop()
print(num)
#
print(45 in num)
print(num.count(2))
#sort
#copy
#reverse
#duplicate num
number =[3,6,2,6,3,84,3,6,9,5]
unique =[]
for i in number:
    if i not in unique:
        unique.append(i)
print(unique)
'''

#tuples
#unchanged
#unpacking

'''number = (1,2,3)
print(number[0])
#dictionaries
#noduplicate,unique key
customer = {
    "name":"preeti",
    "age" :30,
    "dob":3/2008
}
print(customer["name"])
print(customer.get("age"))
print(customer.get("dob",))
#split
phone = input("phone num")
mapping = {
    "1":"one",
    "2":"two",
    "3":"Three",
    "4":"four"
}
for ch in phone:
    phone+=mapping.get(ch)
print(phone)
'''
#function use tab for indentation
'''def greet(name):
    print(f"hello {name}")
    print("thank you")
greet("preeti")#positional agrument
greet("adarsh")
'''
'''def square(number):
    return number*number

result =square(2)
print(result)'''

'''#positonal parameter
def add(a,b):
    print(a+b)

print(add(3,6))

#default parameter
def fun(name="pree"):
    return name
print(fun('Preeti'))
print(fun())

def my_self(age=30):
    return age
print(my_self())
print(my_self(3))

#keyword parameter
def keys(age,name):
    return name ,age
print(keys(age=34,name="vebf"))
print(keys(age=44,name=""""""))
'''
#variable length parameter
def add(*args):
    print(sum(args))

print(add(3,4,6,2,23))











'''def update(x):
    x=8
    print(x)

update(10)

def add(a,b): #formal argument
    c=a+b
    print(c)

add(3,4) #actual argument
add(10,20)

def person(name,age): #formal argument
    print(name)
    print(age)

person("preeti",22) #actual argument

person(age=22,name="preeti") #keyword argument
person(name="preeti",age=22)
person("preeti",age=22) #mixing positional and keyword argument


def info(name,age=18): #default argument
    print(name)
    print(age)
info("preeti",22)
info("preeti")#age=18 by default

def sum(a,b=5,c=10): #default argument
    s=a+b+c
    print(s)    

sum(3,7,4) #all positional argument
sum(3,7)   #c=10 by default
sum(3)     #b=5,c=10 by default
sum(a=3,c=12) #b=5 by default
'''


'''def sum(*b):
 print(sum(b))

print(sum(2,3,4,55,2))'''

'''def person(name,**data):
    print(name)
    
    for i,j in data.items():
        print(i,j)


person('navin',age =22,city ='engineer',mob ='cse')
'''

list = [2,4,5,7,2,3,7,9,0,10]
def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
          even+=i
        else:
           odd+=i
    return odd, even


print(count(list))
# print("the even number count is ",count(even))
# print("the odd number count",count(odd))

            
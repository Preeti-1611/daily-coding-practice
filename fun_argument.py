def update(x):
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
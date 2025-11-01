a =10
def something():
    print("this is local")
    a = 15

    print(a)

something()
print("this is global")
print(a)



b=10
def new():
    global b
    b=23
    print(b)

new()
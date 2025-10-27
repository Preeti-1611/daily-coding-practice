from tabnanny import process_tokens
#
# print("hello world")
# print('*'*10)#it is a long string in one line
# print(('*\n')*10)#if i wnt in new line
# print(('==\n')*10)
# price=10
# print(price)
# name=20 # python is case sensitive
# Name=45
# print(Name)
# print(name)

#multiple variables in one line
a,b,c,d =2,3,7,6
print(a)
print(b)
print(c)
print(d)

def is_bool(a):
    print("you are",a)
    return 'you are in ',a

print(is_bool('True'))
print(is_bool(19))

# def sum(n,n): # parameter must be unique
#     return n+n
# sum(2,6)
# print(sum)

def sum(a,b):
    return a+b
print(sum(23,45))

def cal(*agr):
    return pow(*agr) #
print(cal(2,3))
print(cal(4,2))

print(floor(3.5))






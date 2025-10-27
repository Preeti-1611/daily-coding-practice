# print(~3)
# print(~11)
# print(~5)
#
#
# print(7|4)
# print(8|5)
# print(6|3)

# or
def funo(a,b):
    return a|b

print(funo(7,4))
print(funo(8,5))
print(funo(9,8))
print(funo(10,13))
print(funo(9,12))
# and
def funand(x,y):
    return x&y
print(funand(7,4))
print(funand(8,5))
print(funand(9,8))
print(funand(10,13))
print(funand(9,12))

# xor
def fun_xor(a,b):
    return a^b
print(fun_xor(7,4))
print(fun_xor(8,5))
print(fun_xor(6,3))
print(fun_xor(9,12))

# left shift
print(7<<2)
print(4<<3)
print(5<<3)
print(9<<2)
print(6<<3)

#right shift
print(7>>2)
print(4>>3)
print(5>>3)
print(9>>2)
print(6>>3)
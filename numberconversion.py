num =30
print(bin(num))
print(oct(num))
print(hex(num))


a=0xA
print(bin(a))

b=0b10010011
print(int('0b01110',2))

c=0o67
print(bin(c))

d =int ('0B1010001010',2)
print(d)

def binary(a):
    print(f"The binary from of {a} is",bin(a))
    print(f"The octal from of {a} is",oct(a))
    print(f"The hex from of {a} is ",hex(a))


binary(23)

print(hex(32))

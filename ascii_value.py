'''#ascii
print(ord('a'))
print(ord('A'))
print(ord('z'))

ch = 99
print(chr(ch))

print(ord('z'))


print(chr(120))
print(chr(65))'''

ch = input('enter the alphabet you want the ascii value:')

if 65<= ord(ch)<=90:
    print("this is uppercse alphabet",ord(ch))

elif 97 <= ord(ch)<=122:
    print("this alphabet is lowercase =" ,ord(ch))

else:
    print("give the alphabet only ")



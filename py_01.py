'''price=10
rating= 2.9
name = 'mosh'
print(price)

patient_name = 'john smith'
age= 20
new_patinet = True
print(patient_name)

#input fun
name =input('enter is your name? ')
print('hi '+ name)'''

'''name =input('name please?')
color = input('enter the color ? ')
print(name + ' likes '+ color)
'''

'''birth_year =input('enter your birth year')
print(type(birth_year))
age = 2025-int(birth_year)
print(type(age))
print(age)
'''
'''#use int otherwise it will take as a str
weight = int(input ('enter your weight (in pounds)'))
kilogram =weight *0.453
print('the weight in kilogram',kilogram)'''

'''course = "python is of beginners"
print(course[0])
print(course[-1])
print(course[-3])
print(course[0:4])
print(course[0:])
print(course[:])

print(course)
multiline = 'hi'
#print(multiline)

'''
'''new ="preeti"
print(new)
hi = f'hi {new}'
print(hi)'''

'''#str methods
subject = ('python is programming language')
print(len(subject))
print(subject.upper())
print(subject.lower())
print(subject.capitalize())
print(subject.find('h')) # index
print(subject.find('is'))
print(subject.replace('is','is a'))
print('python' in subject)
print('is' in subject)
print('ina' in subject)

'''

'''print(10/3)
print(10//3)
print(10**3)
print(10%3)
x=10
y=20
x+=20
print(x)
x-=30
print(x)
print(10+4*6**2)
#math fun
x = 2.9
y = 3.4
z= 4.5
print(round(x))
print(round(y))
print(round(z))
#absloute function always returns positive
print(abs(-5.777))'''
'''
''1. Ceil (Ceiling)

Ceiling means rounding UP to the nearest integer.

Even if the number is already close to the next whole number, it goes up.

👉 Example:

ceil(4.2) = 5

ceil(7.9) = 8

ceil(-3.4) = -3 (because -3 is greater than -3.4)

2. Floor

Floor means rounding DOWN to the nearest integer.

It always goes down (towards negative infinity).

👉 Example:

floor(4.2) = 4

floor(7.9) = 7

floor(-3.4) = -4 (because -4 is smaller than -3.4)''
import math
print(math.ceil(4.23))
print(math.floor(-6.7))
print(math.ceil(-6.3))
print(math.ceil(-3.5))
print(math.floor(-5.6))
'''
'''#if statment
is_hot = True
is_cold = False
if is_hot:
     print("its a hot day")
     print("drink more water")
elif is_cold:
    print("its a cold day")
    print("wear cloths")
else:
    print("thank you")
print("enjoy your days")

price = 10000
has_good_credit = True
if has_good_credit:
    payment = 0.1 *price
    print("good Credit")
else:
    payment = 0.2 * price
    print("bad Credit")
print(f"your credit is {payment}")
'''
'''#AND AND OR NOT
has_high_income = True
has_good_credit = False
if has_good_credit or has_high_income:
    print("your are eligible for loan")

name = "preeti"
if len(name)<3:
    print("name must be at least 3 char")
elif len(name)>50:
    print("name must be at most 50 char")
else:
    print("name is good")

weight = int(input("enter your weight"))
unit =input("(L)bs or (K)g : ")
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"you are {converted} kilo")
else:
    converted = weight /0.45
    print(f"you are {converted} pounds")












'''
'''i=0
while i<=5:
   print('* '*i)
    i = i + 1

print("done")
'''
'''guess_num=10
guess_count =0
while guess_count <5:
    guess =int(input('guess the number'))
    guess_count+=1
    if guess == guess_num:
        print("you Win!")
        break
else:
      print("sorry your guess limit is over")
print("thank you")'''


'''
input1 =""
while True:
        input1 = input(">").lower()
        if input1 == "start":
            print("your care is ready to go!")
        elif input1 =="stop":
            print("tour car stops")
         
        elif input1== "help":
            print(start- to start the car
stop - to stop the car
quit - to exit)
        elif input1 == 'quit':
            break
        else:
           print("i am not understanding")
'''
#for loop
'''for item in "python":
     print(item)

for item in [1,3,5]:
    print(item)

for item in ['me', 'you']:
    print(item)

for item in range(10):
    print(item)'''

'''for item in range(5,10,3):
    print(item)

price =[12,23,12,34,12]
sum=0
for i in price:
    sum = sum+i
    i+=1
print("the total price is ",sum)

for x in range(5):
    for y in range(5):
        print(y,x)

num=[5,2,5,2,2]
print(num[0])
for i in num:
  for j in range(i):
      print('x',end ='')
  print('')

'''
'''name =[3,5,7,8,34,5,7]
max = name[0]
for i in name:
    if i > max:
     max = i
print(max)
'''









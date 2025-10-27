#Ask the user for a number N and print the sum of all numbers from 1 to N.

N = int(input('enter the number'))

sum1= 0
for i in range(1,N+1):  #imp
    sum1= sum1+i
print(f"sum of {N} is ",sum1)
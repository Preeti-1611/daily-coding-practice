a = []
n = int(input('How many number  '))

for i in range(n):
    num = int(input(f'Enter number {i+1}: '))
    a.append(num)

print('The numbers are:', a)


while True:
    for i in range(n-1-i):
         if a[i] > a[i+1]:
             temp =a[i]
             a[i]=a[i+1]
             a[i+1]= temp




print('Sorted list:', a)



'''for i in range(n-1):
    for j in range(n-1-i):
       if a[i]>a[i+1]:
           temp = a[i]
           a[i] = a[i+1]
           a[i+1]=temp

print('The numbers are:', a)
'''

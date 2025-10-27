a=[]
n=int(input('enter a number you want in the list:'))
for i in range(n):
    number = int(input('enter a number :'))
    a.append(number)
print('the list is ',a)

# i=0
# min=i
for i in range(n-1):
     min = i
     for j in range(i+1,n-1):
        if a[j]<a[min]:
              min=j  #
     a[i],a[min]=a[min],a[i] #swaping

print('the sorted list ',a)




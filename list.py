empty_list = []
print(empty_list)
print(type(empty_list))

print(len(empty_list))

a =[23,45,2,22,45,43,22]
print(a)
print(a[0])
print(a[-3])
print(a[1:5])
print(a.append(97))
print(a)
print(a.insert(5,677))
print(a)
print(a.extend([244,66,443]))
print(a)


b =[43,56,"preeti",33,21]
print(b)
print(len(b[2]))
print(len(b))
print(b.remove('preeti'))
print(b)
b.pop()
print(b)
print(b.index(56))
print(b)
print(b.append(67))
print(b)

print(b.extend([34,56,89,76,54]))
print(b)
print(b.count('preeti'))
print(b.count(56))
#print(b.index('preeti'))
print(b.sort())


a = [3, 1, 2]
b = a.sort()       # sorts in place
print(a)          # [1, 2, 3] → list is changed
print(b)          # None → method returns nothing


a = [3, 1, 2]
b = sorted(a)     # creates a new sorted list
print(a)          # [3, 1, 2] → original list unchanged
print(b)          # [1, 2, 3] → new list returned

#Use a.sort() if you want to change the original list.

#Use sorted(a) if you want a new sorted list without changing the original.

#Don’t print a.sort() directly, because it will always be None.

d = [3,4,3,2,256,346,7645,65]
print(d)
print(d[::-1])

print(d.reverse())
print(d)

f = a.copy()
print(f)

print(a.pop())
print(a)
print(a.extend([3,5,32,6]))
print(a)
print(a.pop(3))
#print(a.remove(5))
print(a.remove(6))
print(a)

print(a.index(32))
print(a.count(1))

a = [10, 20, 30, 40]

a.append(50)
print(a)   # [10, 20, 30, 40, 50]

a.insert(2, 25)
print(a)   # [10, 20, 25, 30, 40, 50]

a.extend([60, 70])
print(a)   # [10, 20, 25, 30, 40, 50, 60, 70]

a.remove(25)
print(a)   # [10, 20, 30, 40, 50, 60, 70]

a.pop()
print(a)   # [10, 20, 30, 40, 50, 60]  (removes last item)

print(a.index(40))  # 3
print(a.count(20))  # 1

a.sort()
print(a)   # [10, 20, 30, 40, 50, 60]

a.reverse()
print(a)   # [60, 50, 40, 30, 20, 10]

b = a.copy()
print(b)   # [60, 50, 40, 30, 20, 10]

a.clear()
print(a)   # []

g =[4,7,2,4,8,9,4]
print(g)
g.sort()
print(g)
g.reverse()
print(g)

g.sort(reverse = True)
print(g)

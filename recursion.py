# import sys
# sys.setrecursionlimit(200 )
# print(sys.getrecursionlimit())


'''def greet(n):
      for i in range(0,n):
             print("hello",i)
      greet()


greet(10)
'''

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

result = fact(4)
print(result)

# lambda arguments: expression
# mul = lambda a,b:a*b
# print(mul(2,4))

# add = lambda x,y :x+y
# print(mul(4,6))



# def is_even(n):
#     return n%2==0
# nums = [3,4,6,7,8,2,3,6]
# evens = list(filter(is_even,nums))
# print(evens)

nums = [3,4,5,6,7,8]
evens = list(filter(lambda n : n%2==0,nums))

print(evens)


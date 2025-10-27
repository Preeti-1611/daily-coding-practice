#largerst number

number =[]
for i in range(3):
    num = int(input(f"enter the {i} number"))
    number.append(num)
print(number)



#find largest
largest = number[0]
for i in number:
    if i > largest:
        largest = i

print(f"the largest number is {largest}")
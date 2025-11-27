# is

# Meaning: Are they the same exact object in memory?
#  Think like: Are these two things the same person?

# Example:

# a = [1, 2]
# b = a
# print(a is b)   # True


# Because b is just another name for a, same object.

# 2. is not

# Meaning: Are they not the same object?
#  Think like: Are these two different people?

# Example:

# a = [1, 2]
# b = [1, 2]
# print(a is not b)   # True


# Even though values look same, they are stored separately.

# 3. in

# Meaning: Is the item inside the list/string?
# Think like: Is this thing present inside the bag?

# Example:

# fruits = ["apple", "banana", "mango"]
# print("mango" in fruits)   # True

# 4. not in

# Meaning Is the item not inside the list/string?
#  Think like: Is this thing missing from the bag?

# Example:

# fruits = ["apple", "banana", "mango"]
# print("orange" not in fruits)   # True

# | Operator   | Meaning (Simple)    |
# | ---------- | ------------------- |
# | **is**     | Same object?        |
# | **is not** | Different object?   |
# | **in**     | Present inside?     |
# | **not in** | Not present inside? |

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True


#logical and or not
print(3 > 2 and 4<3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

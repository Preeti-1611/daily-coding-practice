s = {3,5,2,2,4}
print(s)
print(s)
print(s)
print(s.add(5))
print(s)
print(s.add(66))
print(s)
print(s.remove(66))
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.add(4)
s.add(87)
print(s)



s={44,63,22,33,44,99,4,2}
print(s)
e ={4,6,2,5,3}
print(e)
print(s.union(e))
b = s.intersection(e)
print(b)
print(s.difference(e))
print(e.difference(s))
print(s.symmetric_difference(e))


#dectionaries
dict = {
    'name':"preeti",
    'age':33,
    'hieght' :1111
}
print(dict)
print(dict.keys())
print(dict.values())
dict['wieght']=23
print(dict)
dict["dob"] = 2/3/2003
print(dict)
dict.pop("name")
print(dict)
dict.popitem()
print(dict)
print(dict.items())
a=dict.keys()
b = dict.values()
print(dict,a,b)

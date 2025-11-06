# polymorphism
class Dog:
    def sound(self):
       print("Dog barks")

class Cat:
    def sound(self):
        print("cat meows")

d1 = Dog()
c1= Cat()

for a in (d1,c1):
    a.sound()




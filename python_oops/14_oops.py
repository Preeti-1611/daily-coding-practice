# poly

class Circle:
    def area(self):
        print("area of circle = pi*r*r ")
    
class Rec:
    def area(self):
        print("area of rectangle")


c = Circle()
r= Rec()

for a in (c,r):
    a.area()
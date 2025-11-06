class Car():
    def __init__(self,name):
        self.name = name
    
    def full_nam(self):
        return self.name
    

class electric_Car(Car):
    def __init__(self,size):
         super().__init__(name)
         self.size = size
     
    def size_(self):
        return f"{self.size}"
    
c1 =Car("this is preeti's car")
print(c1.name)

print(c1.full_nam())


c2 = electric_Car("34km")
print(c2.size_())
'''class students():

    def __init__(self,usn,name):
        self.usn = usn
        self.name = name

    def details(self):
        return f"The student name is {self.name} and USN is {self.usn}"




std1= students("101","preeti")
# print(std1.usn)
# print(std1.name)
print(std1.details())
std2 = students("102","premu")
print(std2.usn)
print(std2.name)
print(std2.details())'''



class Car:
    def __init__(self,brand,model,name):
       self.brand= brand
       self.model = model
       self.name = name
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def summary(self):
        return f"The above car belongs to {self.name}"
    

my_car = Car("Toyota","corolla","preeti")
# print(my_car.brand)
# print(my_car.model)
print(my_car.full_name())
print(my_car.summary())

my_new_car = Car("tata","safari","preeti_nagarale")
print(my_new_car.model)
print(my_new_car.brand)
print(my_new_car.full_name())
print(my_new_car.summary())
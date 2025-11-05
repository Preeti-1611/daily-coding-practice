class Car:
    def __init__(self,brand,model,name):
       self.brand= brand
       self.model = model
       self.name = name

    def get_brand(self):
        return self.brand +"!"
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    
#inheritance
class Electriccar(Car):
    def __init__(self,brand,model,name,battery_size):
        super().__init__(brand,model,name)
        self.battery_size = battery_size


my_tesla = Electriccar("telsa","Model","me","56kwh")
# print(my_tesla.model)
# print(my_tesla.full_name())



my_car = Car("Toyota","corolla","preeti")
# print(my_car.brand)
# print(my_car.model)
print(my_car.full_name())
print(my_car.brand)


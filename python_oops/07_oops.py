# ppolymorphisum
class Car:
    def __init__(self,brand,model,name):
       self.brand= brand
       self.model = model
       self.name = name

    def get_brand(self):
        return self.brand +"!"
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "petrol and desail"
    
    
#inheritance
class Electriccar(Car):
    def __init__(self,brand,model,name,battery_size):
        super().__init__(brand,model,name)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "eletric charge"

my_tesla = Electriccar("telsa","Model","me","56kwh")
# print(my_tesla.model)
# print(my_tesla.full_name())
print(my_tesla.fuel_type())



my_car = Car("Toyota","corolla","preeti")
# print(my_car.brand)
# print(my_car.model)
print(my_car.fuel_type())
print(my_car.full_name())
print(my_car.brand)


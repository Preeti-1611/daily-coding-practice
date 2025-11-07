# class variable

class Car:
    total_cars = 0

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_cars +=1

c1 = Car("toyota","innova")
c2 = Car("honda","city")
c3 = Car("telsa","model S")

print("total cars availbe;",Car.total_cars)


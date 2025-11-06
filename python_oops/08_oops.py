class Vehicale:
    def move(self):
      print("this vehical can move")

class Car(Vehicale):
    def brand(self,name):
        print(f"this car brand is {name}")

c= Car()
c.move() #from parent
c.brand("tata") # from child
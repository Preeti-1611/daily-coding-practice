class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

for pet in (Cat(), Dog()):
    pet.sound()

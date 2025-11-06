# class Animal:
#     def speak(self,name):
#         print(f"animal sound {name}")

# class Dog(Animal):
#     def speak(self):
#         print("dog barks")

# a = Animal()
# d = Dog()

# a.speak("wow")
# d.speak()



class Animal:
    def eat(self,name):
        print(f"eating {name}")

class Dog(Animal):
    def bark(self,name):
        print(f"barking {name}")
d = Dog()
d.eat("without me")
d.bark("why")
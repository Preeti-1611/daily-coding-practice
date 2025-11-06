# setter method
class Dog:
    def __init__(self):
        self.__name = ''

    

    def set_name(self,name):
        if len(name)>0:
            self.__name = name
        else:
            print("name canot be empty!")


    def get_name(self):
        return f"the name is {self.__name}"
    
d1 = Dog()
d1.set_name("murali")
print(d1.get_name())
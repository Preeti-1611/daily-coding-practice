# getter method
class  Employee:

    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
emp1 = Employee("preeti",40000)
emp2 = Employee("murali",400000000000)

print(emp1.name)
# print(emp1.__salary) # you cannot access it bcz itis in the getter
print(emp1.get_salary()) # now you will get bcz you called the method

print(emp2.name)
# print(emp2.__salary)# error
print(emp2.get_salary())

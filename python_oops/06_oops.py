# without getter
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.__marks =  marks #private variable

# std1 = Student("Preeti",89)
# print(std1.name)
# print(std1.__marks)



# with getter
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks
    def get_marks(self):
        return self.__marks

std1 = Student("preeti",23)
# print(std1.marks)
print(std1.get_marks())
print(std1.marks)
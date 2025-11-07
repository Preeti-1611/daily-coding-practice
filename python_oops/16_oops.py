class Student:
    school_name = "ABC school"  #  class variable (shared by all students)

    def __init__(self,name):
        self.name= name  # instance variable (unique for each student)

    

s1 =Student("preeti")
s2 =Student("mayu")

print(s1.school_name) # Output: ABC School
print(s2.school_name) # Output: ABC School